import os
import asyncio
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential
from agent_framework import ChatAgent
from dotenv import load_dotenv

load_dotenv()

async def azure_open_ai_memory_agent():
    my_agent = AzureOpenAIChatClient(
        credential=AzureCliCredential(),
        endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        deployment_name=os.getenv("MODEL_DEPLOYMENT_NAME")
    )

    agent = ChatAgent(
        chat_client=my_agent,
        instructions="You are a helpful assistant."
    )

    thread = agent.get_new_thread()

    result = await agent.run("Hello, my name is Alice", thread=thread)
    print(result.text)

def main():
    asyncio.run(azure_open_ai_memory_agent())


if __name__ == "__main__":
    main()