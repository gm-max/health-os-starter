# Health OS, starter template

Your health data, as plain text files, read by an AI that turns it into daily decisions.

Most of your health data is scattered: bloodwork PDFs, a wearable app, a DEXA scan, a genetics report, a notes app. Nothing reads it *together*. This fixes that. You put everything in one folder of simple files, point an AI at it, and it becomes a coach that knows your whole picture and tells you what to do.

It does three things: **reads** your data and tells you where you stand, **builds** your plans (training blocks, supplement protocol, nutrition), and **coaches** you through decisions. See `EXAMPLES.md` for what each looks like.

No code. If you can edit a text file and paste a prompt, you can run this.

---

## What's in here

```
health-os/
├── README.md              you are here
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

Every file is a template with example (fake) data so you can see the shape. Replace it with yours.

---

## How to set it up (no code)

1. **Get a tool that can read a folder of files.** Any of: Claude (the Cowork desktop app or Claude Code), OpenAI Codex, or any AI you can point at a folder. Free tiers work to start.
2. **Put your data in.** Export what you have (lab portal PDFs, your Whoop/Oura/Garmin, Apple Health, a DEXA report) and paste the numbers into the matching file under `data/`. You don't need everything on day one. Start with bloodwork and one wearable.
3. **Set the AI's role.** Give it `instructions.md` as its system prompt / project instructions (in Claude Cowork or Claude Code, drop this folder in and it reads it automatically; otherwise paste `instructions.md` at the start).
4. **Ask for your read.** "Give me my weekly read." It returns: where you stand, what's flagged, what to do, what to stop, and what's missing.
5. **Keep it alive.** Each time you get a new lab or a new month of wearable data, drop it in the right file and ask again. The picture compounds.

---

## Before you start, read this

- **Your health data is sensitive.** Decide what's cloud vs local. If you use a cloud AI, don't upload anything you wouldn't want stored. Genetics especially (see `data/genetics.md`).
- **This is not medical advice.** It's a tool for organizing your own data and thinking. Anything clinical goes to a doctor.
- **The AI can be wrong.** Make it cite which file each claim comes from, and sanity-check numbers.

---

Built by Max Guérois. I run my own version of this daily. More at [maxguerois.com](https://maxguerois.com), reply to the newsletter and I'll send you updates as the template evolves.
