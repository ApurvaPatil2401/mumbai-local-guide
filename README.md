# Mumbai Local Guide 🇮🇳

A Kiro-powered AI that understands Mumbai slang, food culture, and travel habits using custom local context.

## Features
- Mumbai slang translation
- Street food recommendations
- Local train vs cab advice
- Monsoon-aware travel tips

## Tech Stack
- Python
- Streamlit
- Kiro AI
- Custom context via `.kiro/product.md`

## How It Works
Local Mumbai knowledge is encoded in `product.md`.  
Kiro uses this context to generate responses that reflect real Mumbai behavior instead of generic AI answers.

## Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
