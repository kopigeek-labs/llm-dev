# Set up environment if you saved the API key in a .env file
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

import os
together_api_key = os.getenv('TOGETHER_API_KEY')

url = "http://host.docker.internal:11434/api/generate"

# Store keywords that will be passed to the API
headers = {
    "Authorization": f"Bearer {together_api_key}",
    "Content-Type": "application/json"}

# Choose the model to call
model="togethercomputer/llama-2-7b-chat"

prompt = """
Please write me a birthday card for my dear friend, Andrew.
"""

# Add instruction tags to the prompt
prompt = f"[INST]{prompt}[/INST]"
print(prompt)

# Set temperature and max_tokens
temperature = 0.0
max_tokens = 1024

data = {
    "model": model,
    "prompt": prompt,
    "temperature": temperature,
    "max_tokens": max_tokens
}

data

import requests
response = requests.post(url,
                         headers=headers,
                         json=data)

print(response)

response.json()
response.json()['output']
response.json()['output']['choices']
response.json()['output']['choices'][0]
response.json()['output']['choices'][0]['text']