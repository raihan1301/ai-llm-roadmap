"""
GROQ

OpenAI SDK
    ↓
GROQ_BASE_URL
    ↓
Groq servers
"""

import os

from openai import OpenAI
from dotenv import load_dotenv

"""
for comments see open_ai.py
"""

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url=os.getenv("GROQ_BASE_URL")
)


"""  this below lines are code to list out the models provided by bedrock
models = client.models.list()

for model in models.data:
    if "openai" in model.id.lower():
        print(model.id)
"""


response = client.responses.create(
    model = os.getenv("GROQ_MODEL"),   # for open ai use "BEDROCK_MODEL"
    input = "Explain what Smartops.ca is in one paragraph and how it can help the business?"
)

print("response", response)

print()
print()
print(response.output_text)