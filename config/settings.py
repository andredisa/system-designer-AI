import os
from dotenv import load_dotenv

load_dotenv()

def get_api_keys():
    deepseek_key = os.getenv("DEEPSEEK_API_KEY", "")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY", "")
    return deepseek_key, anthropic_key
