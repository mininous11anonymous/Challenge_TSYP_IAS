import os
from crewai import LLM

def initialize_llm():
    try:
        llm = LLM(
            model=os.getenv("MODEL", "openrouter/google/gemma-2-9b-it"),
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
            temperature=0.4
        )
        return llm
    except Exception as e:
        print(f"[LLM ERROR] {e}")
        print("❌ Missing or invalid OPENROUTER_API_KEY in .env")
        exit(1)
