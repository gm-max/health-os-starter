# Going further: a coach that texts you every morning

The base template is a folder you ask when you want. The next step is making it
come to you: every morning your Health OS reads your data and sends you a short
read on Telegram. No app, no dashboard. It just shows up.

This is the same setup I run daily, stripped down so you can install it in about
five minutes, with no server of your own.

There are two pieces in this folder:

- `coach.py` — reads your files, asks an AI for today's read, sends it to Telegram. Standard library only, no installs.
- `../.github/workflows/daily-coach.yml` — runs `coach.py` on a schedule using a free GitHub Action, so you don't need a computer that's always on.

---

## Read this first: privacy

To have it run on a schedule for free, your data lives in a GitHub repo and gets
sent to an AI API. So:

- **Make your repo private.** Use this template, then set the repo to Private. Never put real health data in a public repo.
- Your files are sent to the AI provider (Anthropic by default) to generate the read. That is the same as pasting them into a chat. Don't include anything you wouldn't.
- **Genetics and anything you consider truly sensitive: leave it out of the automated version**, or run it locally instead (see the bottom). You can still use those files in the manual, on-your-machine version.

If that tradeoff isn't for you, skip the schedule and just run `coach.py` on your
own laptop whenever you want. Same script, nothing leaves your machine except the
one AI call.

---

## Easiest: let your AI set it up (it asks you for each thing it needs)

Same as the main template: paste this to Claude (Cowork or Claude Code) or your agent, and it walks you through it, asking you for one input at a time and telling you exactly where to find it. You don't read a manual; it interviews you.

```text
Set up the "daily Health OS coach" in the going-further/ folder of this repo, so
a free GitHub Action texts me my read every morning on Telegram.

Don't dump all the steps on me. Ask me for ONE thing at a time, in plain
language, and tell me exactly where to get it. The inputs you need from me, in
this order:

1. My Telegram bot token. Tell me to open Telegram, message @BotFather, send
   /newbot, follow the prompts, and paste you the token it gives back.
2. My Telegram chat id. Tell me to message my new bot once (say "hi"), then
   message @userinfobot, and paste you the number it replies with.
3. My Anthropic API key. Tell me to create one at console.anthropic.com and
   paste it.
4. What time I want the text each morning, and my timezone.

After each answer, confirm you've got it and move to the next. Never print my
secrets back to me.

When you have all four:
- Add them as GitHub repo secrets on my copy of this repo with `gh secret set`
  (ANTHROPIC_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID). If `gh` isn't
  installed or signed in, walk me through that first, or offer to run it locally
  on my machine with a .env instead.
- In .github/workflows/daily-coach.yml, uncomment the two schedule lines and set
  the cron to my chosen time converted to UTC (the schedule ships off by default).
- Trigger the workflow once to test it, confirm I got the text, and if it fails,
  read the run logs, tell me the cause in plain words, and fix it.

Then tell me it's done and that it now runs every morning.
```

If you'd rather click through it yourself, here are the same steps by hand.

---

## The 5-minute setup, by hand (texts you every morning, no server)

**1. Create your Telegram bot.**
In Telegram, message [@BotFather](https://t.me/BotFather), send `/newbot`, and
follow the prompts. He gives you a **bot token** that looks like
`123456789:AAExxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`. Keep it.

**2. Get your chat id.**
Open your new bot and send it any message (say "hi"). Then message
[@userinfobot](https://t.me/userinfobot), which replies with your numeric **chat id**.
(That's the simplest way. The bot can only text you after you've messaged it once.)

**3. Get an AI API key.**
Create an [Anthropic API key](https://console.anthropic.com). A daily read costs
a fraction of a cent. (Prefer OpenAI? See "Customize" below.)

**4. Get this template into your own repo.**
At the top of [the repo](https://github.com/gm-max/health-os-starter), click
**Use this template -> Create a new repository**, and set it to **Private**.

**5. Add your three secrets.**
In your new repo: **Settings -> Secrets and variables -> Actions -> New repository secret.**
Add these three:

| Secret name | Value |
|---|---|
| `ANTHROPIC_API_KEY` | your Anthropic key |
| `TELEGRAM_BOT_TOKEN` | the token from BotFather |
| `TELEGRAM_CHAT_ID` | your chat id |

**6. Test it.**
Go to the **Actions** tab, enable workflows if prompted, open **"Daily Health OS coach"**,
and click **Run workflow**. Within a minute you should get a text.

**7. Turn on the daily send.**
The morning schedule ships **off** (so the repo doesn't fail before you've set it up).
Once the test text works, open `.github/workflows/daily-coach.yml`, **uncomment the two
`schedule:` lines**, and set the time (it's in UTC). Commit it, and it now runs every morning.

**8. Put your data in.**
The read is only as good as the folder. Replace the example ("Jane Doe") data with
yours, the easiest way is the paste-this prompt in the main `README.md`. Every file
you add makes tomorrow's text sharper.

---

## Customize

- **The time (and turning the daily send on).** In `../.github/workflows/daily-coach.yml`, uncomment the two `schedule:` lines, then edit the `cron`. GitHub cron is in **UTC**. `"0 7 * * *"` is 07:00 UTC. For 06:00 Paris (winter) use `"0 5 * * *"`.
- **The question.** By default it asks for "your read." To change it (e.g. "plan today's training around my recovery"), add a repository **variable** `COACH_PROMPT`, or edit `DEFAULT_PROMPT` in `coach.py`.
- **The model.** Add a repository **variable** `MODEL` set to a model you have access to (e.g. `claude-sonnet-4-6` for depth, a Haiku model for speed and lower cost).
- **Use OpenAI instead of Anthropic.** Open `coach.py` in your AI tool and say: "swap the `call_ai` function to use the OpenAI API instead, reading `OPENAI_API_KEY`." It's a 10-line change, and the AI will do it for you.

---

## Run it on your own machine instead (most private)

No GitHub, nothing uploaded except the one AI call:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export TELEGRAM_BOT_TOKEN=123456789:AA...
export TELEGRAM_CHAT_ID=987654321
python going-further/coach.py
```

To make that automatic, add one line to your crontab (`crontab -e`):

```cron
0 7 * * *  cd /path/to/health-os && ANTHROPIC_API_KEY=... TELEGRAM_BOT_TOKEN=... TELEGRAM_CHAT_ID=... python3 going-further/coach.py
```

---

## The full version: auto-pull your wearables

What I run goes one step further: it doesn't wait for me to paste data. Every
morning, before the read, it pulls fresh numbers automatically:

- **Whoop, Oura, Garmin** for recovery, sleep, and HRV
- **Withings** for weight and body composition
- **Strava** for training load

The shape is always the same: a small scheduled job calls each service's API,
writes the new numbers into the matching file in `data/`, commits, and then the
coach reads an always-current folder. The only hard part is the one-time auth
with each service (each has its own API and login).

You don't have to write that yourself. Point your AI tool at this repo and paste:

```text
I want my Health OS to auto-update before the daily coach runs. Build me a
script that pulls my [Whoop / Oura / Garmin / Withings / Strava] data via its
API, writes the latest values into the right file under data/ in this repo (same
format as the example data), and commits the change. Walk me through the one-time
authentication for that service step by step, and add it to the GitHub Action so
it runs right before going-further/coach.py each morning.
```

Do one service at a time. Start with whichever wearable you actually wear.

---

Built by Max Guérois. I run this every morning. Questions or you built your own
version? Reply to [the newsletter](https://maxguerois.com) and tell me what you're
tracking, I read every reply.
