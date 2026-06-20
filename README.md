# Health OS, starter template

Your health data, as plain text files, read by an AI that turns it into daily decisions.

Most of your health data is scattered: bloodwork PDFs, a wearable app, a DEXA scan, a genetics report, a notes app. Nothing reads it *together*. This fixes that. You put everything in one folder of simple files, point an AI at it, and it becomes a coach that knows your whole picture and tells you what to do.

It does three things: **reads** your data and tells you where you stand, **builds** your plans (training blocks, supplement protocol, nutrition), and **coaches** you through decisions. See `EXAMPLES.md` for what each looks like.

No code. If you can edit a text file and paste a prompt, you can run this.

---

## Start here (just paste this)

You don't need to download, clone, or set anything up yourself. Claude does all of it for you.

1. **Open [Claude Code](https://claude.com/claude-code) or the Claude Cowork desktop app.** (OpenAI Codex or any agent that can run on your computer works too.) Free tiers are fine to start.
2. **Paste the prompt below.** It grabs this template onto your computer and walks you through putting your own data in. You never have to touch a file yourself.

```text
You are my Health OS, my personal health analyst and coach.

First, set this up for me: get the template at
https://github.com/gm-max/health-os-starter onto my computer in a folder
called "health-os" (clone it with git, or just download the files if git
isn't there), and from now on work inside that folder.

Then read everything in it: start with index.md (the map), then
instructions.md (that is your full role), then profile.md, everything in
data/ and protocol/, dashboard.md, and research/open-questions.md.

These files are filled with example data for a fake person ("Jane Doe"). Help
me replace it with mine, one file at a time, starting with profile.md, then
one bloodwork panel and one wearable. For each file, ask me in plain language
for what you need. If I paste a messy lab PDF or an app export, pull the
numbers out yourself and write them into the right file in the right format.
Never invent a value.

Once my profile, one bloodwork panel, and one wearable are in, give me my
first read: where I stand, what is flagged, what to do this week, what to
stop, and what is missing. Cite which file each point comes from.

Above all: you are not a doctor. Flag anything that needs medical attention
and tell me to see one.
```

That's the whole setup. From here on, whenever you get a new lab or another month of wearable data, paste it to Claude and say "give me my read."

Prefer to do it yourself? Fork the repo or click **Use this template** at the top, drop the folder into your tool, and paste the same prompt.

---

## What's in here

```
health-os/
├── README.md              you are here
├── index.md               the map of your wiki, the AI keeps it current as it grows
├── instructions.md        the important file: turns the AI into your coach
├── EXAMPLES.md            what read / build / coach look like in use
├── LICENSE                MIT, do what you want with it
├── profile.md             who you are, your goals, your targets
├── dashboard.md           a plain-language snapshot the AI keeps updated
├── data/                  your raw results, by source
│   ├── bloodwork.md
│   ├── body-composition.md
│   ├── wearables.md
│   └── genetics.md        (read the privacy note inside)
├── protocol/              what you're doing, and what the AI builds with you
│   ├── supplements.md
│   ├── training.md
│   └── nutrition.md
└── research/
    └── open-questions.md  things you're still figuring out
```

Every file is a template with example (fake) data so you can see the shape. Replace it with yours, or let the prompt above do it with you.

---

## Before you start, read this

- **Your health data is sensitive.** Decide what's cloud vs local. If you use a cloud AI, don't upload anything you wouldn't want stored. Genetics especially (see `data/genetics.md`).
- **This is not medical advice.** It's a tool for organizing your own data and thinking. Anything clinical goes to a doctor.
- **The AI can be wrong.** Make it cite which file each claim comes from, and sanity-check numbers.

---

Built by Max Guérois. I run my own version of this daily. More at [maxguerois.com](https://maxguerois.com), reply to the newsletter and I'll send you updates as the template evolves.
