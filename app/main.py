import streamlit as st
from config.settings import get_api_keys
from core.model_chain import ModelChain
from app.prompts import prompt_guidance

def main():
    st.title("🤖 AI System Architect Advisor")

    st.info(prompt_guidance)

    deepseek_api_key, anthropic_api_key = get_api_keys()

    if not deepseek_api_key or not anthropic_api_key:
        st.warning("🔐 Inserisci le API key nella sidebar.")
        return

    chain = ModelChain(deepseek_api_key, anthropic_api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_prompt := st.chat_input("Descrivi il tuo progetto..."):
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)

        with st.spinner("🤔 Analisi in corso..."):
            deepseek_output = chain.get_deepseek_reasoning(user_prompt)

        with st.spinner("✍️ Generazione risposta..."):
            response = chain.get_claude_response(user_prompt, deepseek_output)
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)

if __name__ == "__main__":
    main()
