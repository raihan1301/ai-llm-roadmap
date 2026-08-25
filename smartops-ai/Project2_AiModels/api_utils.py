import os
import requests
import tiktoken
from openai import OpenAI
from dotenv import load_dotenv

def call_llm(system, user, backend) -> str:
    """
    Receive: system prompt, user prompt, backend name
    ↓ determine backend : bedrock, groq, ollama

    make api call, return only generated text
    """
    load_dotenv()

    if backend == "bedrock":
        api_key = "BEDROCK_API_KEY"
        base_url = "BEDROCK_BASE_URL"
        model = "BEDROCK_MODEL"

        client = OpenAI(
            api_key=os.getenv(api_key),
            base_url=os.getenv(base_url)
        )

        response = client.responses.create(
            model = os.getenv(model),
            instructions = system,   
            input = user
        )

        return response.output_text

    elif backend == "groq":
        api_key = "GROQ_API_KEY"
        base_url = "GROQ_BASE_URL"
        model = "GROQ_MODEL"

        client = OpenAI(
            api_key=os.getenv(api_key),
            base_url=os.getenv(base_url)
        )
        
        response = client.responses.create(
            model = os.getenv(model),
            instructions = system,   
            input = user
        )
        
        return response.output_text

    elif backend == "ollama":
        response = requests.post(
            "http://localhost:11434/api/generate",

            json={
                "model" : "llama3.2",
                "system": system,
                "prompt" : user,
                "stream"  : False,
                "options": {
                    "temperature": 0,
                    "seed": 42
                }
            }
        )

        data = response.json()

        return data["response"]

    else:
        raise ValueError("Invalid Backend")

def count_tokens(text) -> int:
    """
    The purpose is to understand that models don't really charge/process based simply on: They process tokens.
    The exact tokenization depends on the model/tokenizer.
    """
    # encode text
    encoding = tiktoken.get_encoding("o200k_harmony")
    """
    tiktoken is OpenAI's tokenizer library, and GPT-OSS specifically uses the o200k_harmony encoding.
    """

    # count encoded tokens
    tokens = encoding.encode(text)
    """
    encoding.encode(text) = turns the text into token IDs, conceptually something like:
    "I love Python" : [40, 3047, 17852]
    """

    # return count
    return len(tokens)

def estimate_cost(in_tokens, out_tokens, backend) -> float:
    """
    input tokens * input price + output tokens * output price = estimated API cost
    Input: 1,000 tokens ; Output: 500 tokens ; Input price: $1 per million ; Output price: $2 per million
    price is $X per 1 million tokens so divide by million
    """
    if backend == "bedrock":
        input_price = 0.15
        output_price = 0.6

    elif backend == "groq":
        input_price = 0.75
        output_price = 0.3

    elif backend == "ollama":
        return 0

    else:
        raise ValueError("Invalid Backend")

    input_cost = (in_tokens / 1000000) * input_price
    output_cost = (out_tokens / 1000000) * output_price

    total_cost = input_cost + output_cost
    return total_cost

    
def main():
    user_prompt  = "Explain what a neural network is to a software developer in 3 sentences"
    system = "You are a senior AI engineer. Explain technical topics in simple language. " \
    "Keep answers concise. If you do not know something, say you do not know."

    input_tokens = count_tokens(user_prompt) + count_tokens(system)

    bedrock_output = call_llm(system,user_prompt , backend="bedrock")
    bedrock_output_tokens = count_tokens(bedrock_output)
    bedrock_estimated_cost = estimate_cost(input_tokens, bedrock_output_tokens, "bedrock")
    print("**********bedrock_output**************")
    print("Input Tokens:", input_tokens)
    print("Output Tokens:", bedrock_output_tokens)
    print(f"Estimated Cost: ${bedrock_estimated_cost:.8f}")
    print(bedrock_output)

    print("")

    groq_output = call_llm(system,user_prompt , backend="groq")
    groq_output_tokens = count_tokens(groq_output)
    groq_estimated_cost = estimate_cost(input_tokens, groq_output_tokens, "groq")
    print("**********groq_output**************")
    print("Input Tokens:", input_tokens)
    print("Output Tokens:", groq_output_tokens)
    print(f"Estimated Cost: ${groq_estimated_cost:.8f}")
    print(groq_output)

    print("")
    
    ollama_output = call_llm(system, user_prompt , backend="ollama")
    ollama_output_tokens = count_tokens(ollama_output)
    ollama_estimated_cost = estimate_cost(input_tokens, ollama_output_tokens, "ollama")
    print("**********ollama_output**************")
    print(f"Estimated Cost: ${ollama_estimated_cost:.8f}")
    print(ollama_output)


if __name__ == "__main__":
    main()


"""
system means giving instruction how to behave for example AI complaint assistant.
you have to behave professionally, never invent company policy etc
"""