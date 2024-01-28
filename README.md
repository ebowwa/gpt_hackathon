# Text to Short Form Video Content

> **AKA Youtube-Short-inator**

## Overview

We aim to democratize AI by converting long form text into short form video content, like TikTok, YouTube Shorts, and Instagram Reels.

People often don't have time to read long articles and prefer consuming content in short video format. We want to leverage AI to automatically convert text into short, engaging videos.
Solution

Using natural language models like Anthropic's Claude, voice synthesis with Resemble AI, and video generation from Twelve Labs, we can automatically convert text into short video clips.

> see [https://x.com/julesterpak/status/1749205480931557710?s=20] on the importance of edits

## Key aspects

- Natural language model summarizes and edits text into scripts optimized for short video
- Voice synthesis API converts scripts into realistic voice narration  
- Video generation API creates short video clips from images and voiceover

## Challenge

The main challenge is monetizing the service. Possible options:

- Charge per generated video
- Offer freemium model with advanced features for pay
- Build audience then monetize through advertising

## Tools

We utilize several AI services:

- Mistral
- [OpenAI documentation](https://platform.openai.com/docs/plugins/introduction) - Natural language model
- [Resemble AI](https://docs.app.resemble.ai/docs/client_libraries/python/) - Voice synthesis API  
- [Twelve Labs](https://docs.twelvelabs.io/docs/introduction) - Video generation API

## Tech Stack

- Python Flask backend
- Next.js frontend
- Tailwind CSS

## Team

- UI: Skyascii and Jason
- Resemble: SomeGuy, ebowwa
- TwelveLabs: ebowwa, Deepanshu
