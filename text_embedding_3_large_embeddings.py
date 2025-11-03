from openai import OpenAI
from dotenv import load_dotenv
import os 
load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENROUTER_API_KEY")
print(OPENAI_API_KEY)
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPENAI_API_KEY,
)

response = client.embeddings.create(
    model="text-embedding-3-large",
    input="What is the capital city of Nepal ?"
    )
print(response.data[0].embedding)