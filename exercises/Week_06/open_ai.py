"""
BEDROCK

OpenAI SDK
    ↓
BEDROCK_BASE_URL
    ↓
AWS Bedrock
"""

import os

from openai import OpenAI
from dotenv import load_dotenv

"""
Inside open_ai.py: load_dotenv()
searches upward for .env. python-dotenv documents that it looks in the script directory or higher directories.
"""

load_dotenv()

client = OpenAI(
    api_key=os.getenv("BEDROCK_API_KEY"),
    base_url=os.getenv("BEDROCK_BASE_URL")
)

"""
if you leave OpenAI() like this than it will use window api key we setup via setx
"""
"""  this below lines are code to list out the models provided by bedrock
models = client.models.list()

for model in models.data:
    if "openai" in model.id.lower():
        print(model.id)
"""

"""
verify the connection by listing the models Bedrock makes available:
AWS specifically supports client.models.list() through the Bedrock OpenAI-compatible endpoint.
"""

response = client.responses.create(
    model = os.getenv("BEDROCK_MODEL"),   
    input = "Explain what Smartops.ca is in one paragraph and how it can help the business?"
)

print("response", response)

"""
as i said response contains many other things here is the output
=None, prompt_cache_options=None, prompt_cache_retention=None, reasoning=None, safety_identifier=None, service_tier='default', 
status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity='medium'), 
top_logprobs=None, truncation='disabled', 
usage=ResponseUsage(input_tokens=84, input_tokens_details=InputTokensDetails(cache_write_tokens=None, cached_tokens=0), 
output_tokens=228, output_tokens_details=OutputTokensDetails(reasoning_tokens=77), total_tokens=312), user=None)
"""
print()
print()
print(response.output_text)

"""
OpenAI() creates a client that your Python application uses to communicate with OpenAI. 
It finds your API key from the OPENAI_API_KEY environment variable. 

client.responses.create() sends your input to the selected model. 
OpenAI returns a response object, and 

response.output_text gives you the generated text that you print to the terminal.

print(response) : You'll see that OpenAI doesn't actually return only text.
It returns a larger structured Python object containing information around the response.

the API response contains metadata and structured information; output_text is just the convenient text portion.
"""


"""
AWS currently describes them like this: Sol is the most capable model for harder reasoning/coding/agentic work; 
Terra is the balanced general-purpose option; 
Luna is the fastest and lowest-cost option for high-volume tasks such as classification and summarization
"""