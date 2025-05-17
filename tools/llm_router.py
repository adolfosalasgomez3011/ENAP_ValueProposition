import os, requests, openai
from dotenv import load_dotenv

load_dotenv()

def query_llm(prompt, model='llama3'):
    provider = os.getenv('LLM_PROVIDER', 'ollama')
    if provider == 'openai':
        openai.api_key = os.getenv('OPENAI_API_KEY')
        response = openai.ChatCompletion.create(
            model='gpt-4', messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    else:
        res = requests.post('http://localhost:11434/api/generate', json={'model': model, 'prompt': prompt})
        return res.json().get('response', 'No response')
