import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY")
)

response = client.responses.create(
    model=os.getenv("LLM_MODEL"),
    instructions="You are Jason from GTA 6, answer question from big fan of GTA series.",
    input="Would you like to meet Micheal, Franklin or Trevor in your story in GTA 6?",
)
print(response.output_text)
