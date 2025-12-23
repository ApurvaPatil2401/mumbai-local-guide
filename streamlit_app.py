import streamlit as st
from openai import OpenAI

# Load local context
with open(".kiro/product.md", "r", encoding="utf-8") as f:
    PRODUCT_CONTEXT = f.read()

with open(".kiro/system.md", "r", encoding="utf-8") as f:
    SYSTEM_CONTEXT = f.read()

client = OpenAI()

st.set_page_config(page_title="Mumbai Local Guide", page_icon="🚆")

st.title("Mumbai Local Guide 🚆🌧️")
st.caption("Understands Mumbai slang, food, and travel habits")

query = st.text_input(
    "Ask something Mumbai-specific",
    placeholder="e.g. Best way to reach Churchgate at 6 PM?"
)

if query:
    with st.spinner("Thinking like a Mumbaikar..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_CONTEXT},
                {"role": "system", "content": PRODUCT_CONTEXT},
                {"role": "user", "content": query}
            ]
        )

    st.success(response.choices[0].message.content)
