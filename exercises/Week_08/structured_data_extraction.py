from openai import OpenAI
from pydantic import BaseModel

import os
from dotenv import load_dotenv


class ResearchPaperExtraction(BaseModel):
    title: str
    authors : list[str]
    abstract : str
    keywords : list[str]


def main():
    load_dotenv()

    api_key = "GROQ_API_KEY"
    base_url = "GROQ_BASE_URL"
    model = "GROQ_MODEL"

    client = OpenAI(
        api_key=os.getenv(api_key),
        base_url=os.getenv(base_url),
        timeout=30.0,
        max_retries=0
    )

    response = client.responses.parse(
        model=os.getenv(model),
        input=[
            {
                "role": "system",
                "content": "You are an expert at structured data extraction. You will be given unstructured text from a research paper \
                    and should convert it into the given structure."
            },
            {
                "role": "user",
                "content": (
                    "Attention Is All You Need by Ashish Vaswani, Noam Shazeer, "
                    "Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, "
                    "Łukasz Kaiser, and Illia Polosukhin. We propose the "
                    "Transformer, a sequence transduction architecture based "
                    "entirely on attention. Keywords: transformers, attention, "
                    "sequence transduction."
                ),
            }
        ],
        text_format=ResearchPaperExtraction,
    )

    research_paper = response.output_parsed
    print(research_paper.model_dump_json(indent=2))

main()