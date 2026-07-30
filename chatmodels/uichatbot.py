import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

st.title("🤖 AI Chatbot")

model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.9
)

# Mode -> system prompt mapping (same as original script)
modes = {
    "Sad AI chatbot": "You are a sad AI assistant.",
    "Funny AI chatbot": "You are a funny AI assistant.",
    "Angry AI chatbot": "You are an angry AI assistant.",
}

st.subheader("Choose your AI mode")
choice = st.radio(
    "choose your ai mode",
    options=list(modes.keys()),
    label_visibility="collapsed"
)

# (Re)initialize chat history when mode changes or on first run
if "current_mode" not in st.session_state or st.session_state.current_mode != choice:
    st.session_state.current_mode = choice
    st.session_state.messages = [
        SystemMessage(content=modes[choice])
    ]

# Display chat history (skip the SystemMessage, it's not shown in UI)
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# Chat input
prompt = st.chat_input("you: ")

if prompt:
    # Append and show user message
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    # Get response from model
    response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))

    # Show bot response
    with st.chat_message("assistant"):
        st.write(response.content)