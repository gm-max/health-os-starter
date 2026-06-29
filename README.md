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

Then give me a short, prioritized plan for what to add next to make this
more useful, and offer to walk me through the first step.

Above all: you are not a doctor. Flag anything that needs medical attention
and tell me to see one.
```

That's the whole setup. From here on, whenever you get a new lab or another month of wearable data, paste it to Claude and say "give me my read."

**Just want to see it work first?** Before you change anything, ask it "give me my read." It runs on the example ("Jane Doe") data, so you see the output in about 30 seconds, then you decide if it's worth putting yours in.

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
│   ├── nutrition.md
│   └── peptides.md        clinician-supervised compounds, GLP-1s and similar (safety note inside)
├── research/
│   └── open-questions.md  things you're still figuring out
└── going-further/         optional: make it text you every morning (its README has the setup)
```

Every file is a template with example (fake) data so you can see the shape. Replace it with yours, or let the prompt above do it with you.

---

## Grow it over time

The first read works with just your profile, one bloodwork panel, and one wearable. After that, the AI tells you what to add next. The usual path, easiest first:

1. Body composition (a DEXA scan or a smart scale)
2. Your current supplements and training
3. Nutrition, and any family history
4. Older bloodwork, so it can see trends
5. Genetics, last and carefully (see the privacy note in `data/genetics.md`)

You never format anything. Paste a raw lab PDF or an app export and the AI files it, updates the dashboard, and keeps the index current. The picture compounds: every add makes the next read sharper.

---

## Going further: a coach that texts you every morning

The folder answers when you ask. The next step is making it come to you: every morning it reads your data and sends you a short read on Telegram. No app, no dashboard, it just shows up. It's the same setup I run daily, and you can install the stripped-down version in about five minutes, with no server of your own.

A free GitHub Action does the scheduling, so nothing of yours has to stay on. There's also a path to auto-pull your Whoop, Withings, or Strava data so the folder updates itself before each morning's read.

How-to: **[going-further/](going-further/README.md)**.

---

## Before you start, read this

- **Your health data is sensitive.** Decide what's cloud vs local. If you use a cloud AI, don't upload anything you wouldn't want stored. Genetics especially (see `data/genetics.md`).
- **This is not medical advice.** It's a tool for organizing your own data and thinking. Anything clinical goes to a doctor.
- **The AI can be wrong.** Make it cite which file each claim comes from, and sanity-check numbers.

---

If this is useful: **star the repo** (it helps others find it), and **[subscribe at maxguerois.com](https://maxguerois.com)**. I send the automated version, template updates, and what I'm learning building my own health in the open, about one email a week. Reply to any of them and tell me what you're tracking. I read every one.

Built by Max Guérois. I run this daily. Fork it, make it yours.
