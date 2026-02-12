import streamlit as st
import os
from groq import Groq

# Load local context
with open(".kiro/product.md", "r", encoding="utf-8") as f:
    PRODUCT_CONTEXT = f.read()

with open(".kiro/system.md", "r", encoding="utf-8") as f:
    SYSTEM_CONTEXT = f.read()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="Mumbai Local Guide", page_icon="🚆")
hide_style = """
    <style>
    /* Hide the Streamlit header and GitHub/Fork icons */
    header {visibility: hidden;}
    
    /* Optional: reduce top padding after hiding header */
    .block-container {padding-top: 2rem;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

st.title("Mumbai Local Guide 🚆🌧️")
st.caption("Understands Mumbai slang, food, and travel habits")

query = st.text_input(
    "Ask something Mumbai-specific",
    placeholder="e.g. Best way to reach Churchgate at 6 PM?"
)

if query:
    with st.spinner("Thinking like a Mumbaikar..."):
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": SYSTEM_CONTEXT},
                {"role": "system", "content": PRODUCT_CONTEXT},
                {"role": "user", "content": query}
            ]
        )

    st.success(response.choices[0].message.content)
