# Mumbai Local Guide 🏙️

Mumbai Local Guide is an AI-powered travel assistant designed to help users navigate Mumbai with practical, context-aware recommendations. It provides guidance on local transportation, street food, Mumbai slang, and monsoon travel using curated Mumbai-specific knowledge instead of generic travel advice.

## Features

- 🚆 Local train vs. cab recommendations
- 🍛 Street food suggestions
- 💬 Mumbai slang explanations
- 🌧️ Monsoon-aware travel guidance
- 🧠 Context-aware responses tailored for Mumbai

---

## Live Demo

Built with **Streamlit**.
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mumbai-local-guide-4rygljnmqmapsawqtpoy9c.streamlit.app/)

Run locally:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
---

## AWS Builder Center Experiment

An experimental implementation using **Amazon Bedrock** and **Llama 4 Maverick** was built while exploring AWS Builder Center.

The AWS version is available in the **`aws-experiment`** branch of this repository so the `main` branch continues to host the stable Streamlit version.

## Demo

https://github.com/user-attachments/assets/3a47c7ae-c01d-4208-be97-3531e84ecb76


---
## Architecture

```text
                User
                  │
                  ▼
            Streamlit UI
                  │
                  ▼
      Prompt + Mumbai Knowledge
   (.kiro/system.md + context files)
                  │
                  ▼
           AI Language Model
                  │
                  ▼
      Mumbai-specific Response
```

---

## Tech Stack

- Python
- Streamlit
- Groq API
- Llama 3
- Kiro AI
- Prompt Engineering
- Amazon Bedrock Runtime
- Llama 4 Maverick

---

## How It Works

- Loads curated Mumbai-specific knowledge.
- Combines the user's question with contextual prompts.
- Sends the enriched prompt to the language model.
- Returns practical recommendations tailored for Mumbai.

---

## Example Questions

- Best vada pav near Dadar?
- Should I take a local train or cab from Andheri at 6 PM?
- What does "Scene kya hai?" mean?
- Is it safe to travel during heavy rain?
- Hidden places to visit in Mumbai?


## Future Improvements

- Live weather integration
- Real-time train status
- Maps integration
- Voice interface
- Multilingual support (English, Hindi, Marathi)

