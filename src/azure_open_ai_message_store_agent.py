import os
import asyncio
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential
from agent_framework import ChatAgent, ChatMessageStore
from dotenv import load_dotenv

load_dotenv()

def create_message_store():
    return ChatMessageStore()

async def azure_open_ai_message_store_agent():
    credential = AzureCliCredential()
    my_agent = AzureOpenAIChatClient(
        credential=credential,
        endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        deployment_name=os.getenv("MODEL_DEPLOYMENT_NAME")
    )

    agent = ChatAgent(
        chat_client=my_agent,
        instructions="You are a helpful assistant.",
        chat_message_store_factory=create_message_store
    )

    # Create a single message store instance to use throughout
    message_store = agent.chat_message_store_factory()

    # Use the same thread for conversation continuity
    thread = agent.get_new_thread()

    result = await agent.run("Hello, my name is Alice", thread=thread)
    await message_store.add_messages(result.messages)

    result = await agent.run("What is the weather like today?", thread=thread)
    await message_store.add_messages(result.messages)

    for message in await message_store.list_messages():
        print(f"{message.role}: {message.text}")

def main():
    asyncio.run(azure_open_ai_message_store_agent())


if __name__ == "__main__":
    main()