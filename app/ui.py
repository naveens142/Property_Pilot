import streamlit as st
from rag import ask_question

st.set_page_config(page_title="Property Chatbot")

st.title("🏠 Property  Chatbot")

question = st.text_input("Ask about properties:")

if question:
    with st.spinner("Searching..."):
        answer = ask_question(question)
    st.write(answer)
