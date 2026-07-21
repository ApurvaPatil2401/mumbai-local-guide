import streamlit as st
import boto3

# Load context
with open(".kiro/mumbai_knowledge.md", "r", encoding="utf-8") as f:
    PRODUCT_CONTEXT = f.read()

with open(".kiro/system.md", "r", encoding="utf-8") as f:
    SYSTEM_CONTEXT = f.read()

# Combine both system prompts
SYSTEM_PROMPT = SYSTEM_CONTEXT + "\n\n" + PRODUCT_CONTEXT

# Bedrock client
bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-west-2"
)

modelId="arn:aws:bedrock:us-west-2:442042535736:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0"
MODEL_ID = modelId
st.set_page_config(page_title="Mumbai Local Guide", page_icon="🚆")
with st.sidebar:
    st.header("🚆 Quick Examples")

    st.markdown("### 🍛 Food")
    st.code("Best Misal Pav near Thane?")

    st.markdown("### 🚆 Commute")
    st.code("Local or cab from Andheri at 6 PM?")

    st.markdown("### ☔ Monsoon")
    st.code("Travel from Powai to Bandra in heavy rain")

    st.markdown("### 🗣️ Slang")
    st.code("What does 'Scene kya hai?' mean?")

    st.divider()

    st.markdown("### 🧠 AI Stack")

    st.success("""
Amazon Bedrock

Llama 4 Maverick
               
Context Engineering

Prompt Engineering

Streamlit
""")
st.title("Mumbai Local Guide 🏙️ 🚆🌧️")
st.caption("Powered by Amazon Bedrock • Llama 4 Maverick \n\n • local Mumbai Assistant for Mumbai travel, food, slang and daily commuting.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.markdown("### 💡 Try asking")

col1, col2 = st.columns(2)

with col1:
    st.info("🍔 Best street food near Dadar?")

with col2:
    st.info("🚆 Local or cab from Andheri?")

# Chat input
if prompt := st.chat_input(" Ask about trains, food, slang or monsoon..."):

    # Show user message
    st.chat_message("user").markdown(prompt)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Convert chat history to Bedrock format
    conversation = []
    for msg in st.session_state.messages:
        conversation.append({
            "role": msg["role"],
            "content": [
                {"text": msg["content"]}
            ]
        })

    # Call Bedrock
    with st.spinner("Asking a local Mumbaikar..."):
        response = bedrock.converse(
            modelId=MODEL_ID,
            system=[
                {"text": SYSTEM_PROMPT}
            ],
            messages=conversation,
            inferenceConfig={
                "temperature": 0.7,
                "maxTokens": 512
            }
        )

    # Extract reply
    reply = response["output"]["message"]["content"][0]["text"]

    # Show assistant message
    st.chat_message("assistant").markdown(reply)

    # Save assistant reply
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

st.caption(
    "Recommendations are based on local knowledge and LLM reasoning. "
    "Business availability and traffic conditions may change."
)