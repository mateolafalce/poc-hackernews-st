<div align="center">

# HackerNews Story Teller

![video](./public/sora.gif)

</div>

An automated pipeline that transforms trending Hacker News articles into engaging YouTube Shorts. The system fetches top stories from Hacker News, generates compelling scripts with a San Francisco Bay Area vibe using OpenAI, creates cinematic scene descriptions, and produces pixel art-style videos using OpenAI's Sora AI, all optimized for the vertical 9:16 YouTube Shorts format.

**State of the project:** Pause at the moment

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
python3 main.py
```