#!/usr/bin/env python3
"""
Daily Health OS coach -> Telegram.

Reads your Health OS folder, asks an AI for today's read, and texts it to you.
Standard library only: no `pip install` needed. Runs anywhere Python 3 runs
(your laptop, a cron job, or the included GitHub Action).

It needs three things, passed as environment variables:

    ANTHROPIC_API_KEY    your Anthropic API key   (https://console.anthropic.com)
    TELEGRAM_BOT_TOKEN   your bot token from @BotFather
    TELEGRAM_CHAT_ID     your chat id (the guide shows how to get it)

Optional:
    MODEL                Anthropic model id (default below). Set to one you have access to.
    COACH_PROMPT         override the daily question (default: "give me my read")

See going-further/README.md for the 5-minute setup. To use OpenAI instead of
Anthropic, ask your AI to swap the `call_ai` function. That's the only change.
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

# Files the coach reads, in order. Everything else in the folder is ignored.
CORE_FILES = ["index.md", "instructions.md", "profile.md", "dashboard.md"]
CORE_DIRS = ["data", "protocol", "research"]

DEFAULT_MODEL = "claude-sonnet-4-6"
DEFAULT_PROMPT = (
    "Give me my read for today, as a short message I can read on my phone. "
    "Lead with where I stand on the metrics that matter now, then anything "
    "flagged, then 1 to 3 concrete things to do today. Keep it tight. "
    "Cite which file each point comes from. You are not a doctor; flag "
    "anything that needs one."
)
TELEGRAM_MAX = 4000  # stay under Telegram's 4096 hard cap


def die(msg: str) -> None:
    """Fail loud. A silent failure is the worst failure."""
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def env(name: str, required: bool = True, default: str = "") -> str:
    # Treat a set-but-empty variable (e.g. an unset GitHub Action `vars.MODEL`)
    # the same as missing, so the default still applies.
    val = os.environ.get(name, "").strip() or default
    if required and not val:
        die(f"missing required environment variable: {name}")
    return val


def read_folder(root: Path) -> str:
    """Concatenate the Health OS files into one labelled blob for the AI."""
    parts: list[str] = []
    for name in CORE_FILES:
        p = root / name
        if p.is_file():
            parts.append(f"===== {name} =====\n{p.read_text(encoding='utf-8')}")
    for d in CORE_DIRS:
        for p in sorted((root / d).glob("*.md")):
            parts.append(f"===== {d}/{p.name} =====\n{p.read_text(encoding='utf-8')}")
    if not parts:
        die("no Health OS files found. Run this from your health-os folder "
            "(or set the path), and make sure instructions.md exists.")
    return "\n\n".join(parts)


def call_ai(system: str, user: str) -> str:
    """Call the Anthropic Messages API with stdlib only. Returns the text."""
    api_key = env("ANTHROPIC_API_KEY")
    model = env("MODEL", required=False, default=DEFAULT_MODEL)
    body = json.dumps({
        "model": model,
        "max_tokens": 1200,
        "system": system,
        "messages": [{"role": "user", "content": user}],
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")
        die(f"Anthropic API {e.code}. If this is a model error, set the MODEL "
            f"env var to one you have access to. Details: {detail}")
    except urllib.error.URLError as e:
        die(f"could not reach the Anthropic API: {e}")
    try:
        return "".join(b.get("text", "") for b in data["content"]).strip()
    except (KeyError, TypeError):
        die(f"unexpected Anthropic response: {json.dumps(data)[:500]}")


def split_chunks(text: str, limit: int = TELEGRAM_MAX) -> list[str]:
    """Split into Telegram-sized chunks at natural boundaries."""
    chunks: list[str] = []
    remaining = text.strip()
    while len(remaining) > limit:
        cut = remaining.rfind("\n\n", 0, limit)
        if cut <= 0:
            cut = remaining.rfind("\n", 0, limit)
        if cut <= 0:
            cut = limit
        chunks.append(remaining[:cut].strip())
        remaining = remaining[cut:].strip()
    if remaining:
        chunks.append(remaining)
    return chunks


def send_telegram(text: str) -> None:
    """Send a message via the Telegram Bot API. Splits long messages."""
    token = env("TELEGRAM_BOT_TOKEN")
    chat_id = env("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    chunks = split_chunks(text)
    if not chunks:
        die("nothing to send (the AI returned an empty message).")
    for i, chunk in enumerate(chunks):
        payload = json.dumps({"chat_id": chat_id, "text": chunk,
                              "disable_web_page_preview": True}).encode("utf-8")
        req = urllib.request.Request(
            url, data=payload,
            headers={"content-type": "application/json"}, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                resp.read()
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")
            die(f"Telegram API {e.code}. Check TELEGRAM_BOT_TOKEN and "
                f"TELEGRAM_CHAT_ID. Details: {detail}")
        except urllib.error.URLError as e:
            die(f"could not reach Telegram: {e}")
        if i < len(chunks) - 1:
            time.sleep(0.5)  # be gentle between message parts


def main() -> None:
    # Run from the repo root by default; override with HEALTH_OS_DIR.
    root = Path(os.environ.get("HEALTH_OS_DIR", Path(__file__).resolve().parent.parent))
    folder = read_folder(root)
    instructions = (root / "instructions.md").read_text(encoding="utf-8")
    prompt = env("COACH_PROMPT", required=False, default=DEFAULT_PROMPT)

    system = (
        instructions
        + "\n\n---\nYou are sending a single short Telegram message. Plain text "
          "only, no markdown formatting characters. Keep it scannable on a phone."
    )
    user = f"Here are my Health OS files:\n\n{folder}\n\n---\n{prompt}"

    message = call_ai(system, user)
    send_telegram(message)
    print("Sent today's read to Telegram.")


if __name__ == "__main__":
    main()
