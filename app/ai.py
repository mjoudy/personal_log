import openai
import os
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def categorize_text(log_text):
    prompt = f"""
    Analyze the following text and categorize into:
    - Tasks
    - Feelings
    - Diary
    - Questions
    
    Provide output as JSON:
    {{
        "tasks": "...",
        "feelings": "...",
        "diary": "...",
        "questions": "..."
    }}
    
    Text: {log_text}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
