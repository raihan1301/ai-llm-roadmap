"""
ollama run llama3.2 : You'll get an interactive prompt. in terminal

ollama list : all the models you downloaded

ollama ps : to inspect a currently loaded/running model and whether it's using CPU/GPU resources. 
Ollama documents ollama ps for checking model execution/offloading.

Ollama documents the local API at that address.
"""
"""
we will see the native Ollama API first rather than hiding it behind the OpenAI SDK.
"""
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model" : "llama3.2",
        "prompt" : "What is SmartOps.ca and how does it help businesses in one paragraph?",
        "stream"  : False,
        "options": {
            "temperature": 0,
            "seed": 42
        }
    }
)

data = response.json()

print(data["response"])


"""
Answer comes different for smae prompt with little wording changed
that called hallucinations

ollama does not automatically browse the web : the model has to rely on whatever patterns/knowledge are already inside its weights.

It may have inferred something plausible from:and happened to land close to reality.
Then on the next run, it inferred something else like real estate.
That is a textbook hallucination:

Ollama's model parameters include temperature, and its documented default is around 0.8. 
Higher temperature allows more variation in token selection. Ollama also supports a seed; using a fixed seed can make the same prompt 
reproduce the same text more consistently.
"""

"""
Version 1:
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model" : "llama3.2",
        "prompt" : "What is SmartOps.ca and how does it help businesses in one paragraph?",
        "stream"  : False
    }
)

Answer 1:
I couldn't find any information on "SmartOps.ca". It's possible that it's a private or local business, or perhaps a website or platform 
that isn't well-known. Can you provide more context or details about SmartOps.ca? 
This will allow me to better assist you and provide a more accurate answer.
"""

"""
version2:
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": "What is SmartOps.ca and how does it help businesses?",
        "stream": False,
        "options": {
            "temperature": 0,
            "seed": 42
        }
    }
)

Answer 2:
I couldn't find any information on "SmartOps.ca". It's possible that it's a new or niche platform, or 
it may not be well-known. Can you provide more context or details about SmartOps.ca? 
I'll do my best to provide an answer once I have more information.
"""

"""
But here's the crucial distinction:
More consistent does not mean more correct. 

If the model doesn't know SmartOps, temperature 0 could simply make it consistently give the same wrong answer.
That's a very important AI-engineering lesson.

An LLM can give one apparently correct answer and then a completely different incorrect answer to a similar question 
because generation is probabilistic and the model is not automatically verifying facts or browsing the web.
"""