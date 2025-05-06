import streamlit as st

def display_message(role: str, content: str):
    with st.chat_message(role):
        st.markdown(content)

def show_expanders(reasoning: str, analysis: str):
    with st.expander("🤖 DeepSeek Reasoning", expanded=True):
        st.markdown(reasoning)

    with st.expander("📊 Technical Analysis", expanded=True):
        st.markdown(analysis)
