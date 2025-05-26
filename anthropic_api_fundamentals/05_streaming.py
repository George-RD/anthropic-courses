# My async streaming chatbot

from dotenv import load_dotenv
from anthropic import AsyncAnthropic
import asyncio

#load environment variable
load_dotenv()

green = '\033[32m'
reset = '\033[0m'

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = AsyncAnthropic()

message_history = []
async def chat_messaging(role,text):
    message_history.append({"role":role,"content":text+"\n"})
    #print("\n"+text+"\n")
    async with client.messages.stream(
        max_tokens=500,
        messages=message_history,
        model="claude-3-haiku-20240307"
    ) as stream:
        async for text in stream.text_stream:
            print(green + text + reset,flush=True,end="")
        message_history.append({"role":"assistant", "content":await stream.get_final_text()})
        print("\n")

async def main():
    while True:
        user_in = input("User:")
        if user_in == "q" or user_in == "":
            break
        else:
            await chat_messaging("user",user_in)

asyncio.run(main())