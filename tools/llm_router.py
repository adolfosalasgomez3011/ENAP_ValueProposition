import os, requests, openai
import json
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
        res = requests.post(
            'http://localhost:11434/api/generate',
            json={'model': model, 'prompt': prompt},
            stream=True
        )

        output = ""
        for line in res.iter_lines():
            if line:
                chunk = json.loads(line.decode("utf-8"))
                output += chunk.get("response", "")
        return output
