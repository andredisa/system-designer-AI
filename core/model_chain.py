from openai import OpenAI
import anthropic
from agno.agent import Agent, RunResponse
from agno.models.anthropic import Claude
from config.constants import DEEPSEEK_MODEL, CLAUDE_MODEL
import streamlit as st
import time

class ModelChain:
    def __init__(self, deepseek_api_key: str, anthropic_api_key: str):
        self.client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")
        claude_model = Claude(
            id=CLAUDE_MODEL,
            api_key=anthropic_api_key,
            system_prompt="""
Given the user's query and the DeepSeek reasoning:
1. Analyze architecture decisions
2. Generate roadmap
3. Create technical specification in markdown
4. Include mermaid.js diagram descriptions
"""
        )
        self.agent = Agent(model=claude_model, markdown=True)

    def get_deepseek_reasoning(self, user_input: str) -> tuple[str, str]:
        try:
            start = time.time()
            system_prompt = "You are an expert software architect..."  # Usa il tuo prompt completo qui
            response = self.client.chat.completions.create(
                model=DEEPSEEK_MODEL,
                messages=[{"role": "system", "content": system_prompt},
                          {"role": "user", "content": user_input}],
                max_tokens=3000
            )
            reasoning = response.choices[0].message.reasoning_content
            analysis = response.choices[0].message.content

            st.expander("DeepSeek Reasoning", expanded=True).markdown(reasoning)
            st.expander("Technical Analysis", expanded=True).markdown(analysis)
            st.caption(f"⏱️ {time.time() - start:.1f}s")
            return reasoning, analysis
        except Exception as e:
            st.error(f"DeepSeek error: {e}")
            return "", ""

    def get_claude_response(self, user_input: str, deepseek_output: tuple[str, str]) -> str:
        try:
            reasoning, analysis = deepseek_output
            message = f"User Query: {user_input}\nDeepSeek Reasoning: {reasoning}\nAnalysis: {analysis}"
            response: RunResponse = self.agent.run(message=message)
            st.markdown(response.content)
            return response.content
        except Exception as e:
            st.error(f"Claude error: {e}")
            return "Errore Claude"
