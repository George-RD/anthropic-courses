import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
my_api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic()

my_first_message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hi there! Give me a concise laugh!"}
    ]
)

print(my_first_message.content[0].text)