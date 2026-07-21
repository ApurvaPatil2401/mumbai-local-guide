# Mumbai Local Guide 🏙️

Mumbai Local Guide is a local AI assistant powered by Amazon Bedrock. It combines prompt engineering with curated Mumbai-specific knowledge to provide practical recommendations for commuting, food, local slang, and monsoon travel instead of generic travel advice.

## Features
- Mumbai slang translation
- Street food recommendations
- Local train vs cab advice
- Monsoon-aware travel tips

## Demo

Coming soon.

## Architecture

```text
                 User
                   │
                   ▼
            Streamlit UI
                   │
                   ▼
      Prompt + Mumbai Knowledge
          (.kiro/system.md
       + mumbai_knowledge.md)
                   │
                   ▼
     Amazon Bedrock Runtime API
                   │
                   ▼
          Llama 4 Maverick
                   │
                   ▼
          Mumbai-specific Reply
```
## Tech Stack
- Python
- Streamlit
- Kiro AI
- Amazon Bedrock Runtime
- Llama 4 Maverick
- AWS SDK for Python (boto3)


## How It Works

- Local Mumbai knowledge is stored in `.kiro/mumbai_knowledge.md`.
- System behavior is controlled through `.kiro/system.md`.
- The application combines the user's query with the curated Mumbai context.
- Amazon Bedrock invokes the Llama 4 Maverick foundation model.
- The model generates practical, Mumbai-specific responses.

## Example Questions

- Best vada pav near Dadar?
- Should I take a local or cab from Andheri at 6 PM?
- What does "Scene kya hai?" mean?
- Travelling from Powai during heavy rain.

## Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
<<<<<<< HEAD
## Try demo:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mumbai-local-guide-4rygljnmqmapsawqtpoy9c.streamlit.app/)
=======

## Future Improvements

- Live weather integration
- Real-time train status
- Maps integration
- Voice input
- Multilingual support (Marathi, Hindi, English)

## Why Amazon Bedrock?

This project demonstrates how Amazon Bedrock can be used to build a domain-specific AI assistant through context engineering and prompt design without requiring model fine-tuning.
>>>>>>> 7226114 (Migrate Mumbai Local Guide to Amazon Bedrock)
