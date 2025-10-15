import asyncio
from foundry_agent import foundry_agent
from foundry_persistent_agent import foundry_persistent_agent
from foundry_streaming_agent import foundry_streaming_agent
from azure_open_ai_chat_agent import azure_open_ai_chat_agent
from azure_open_ai_responses_agent import azure_open_ai_responses_agent
from azure_open_ai_memory_agent import azure_open_ai_memory_agent
from azure_open_ai_message_store_agent import azure_open_ai_message_store_agent


def main():
    asyncio.run(foundry_agent())
    asyncio.run(foundry_persistent_agent())
    asyncio.run(foundry_streaming_agent())
    asyncio.run(azure_open_ai_chat_agent())
    asyncio.run(azure_open_ai_responses_agent())
    asyncio.run(azure_open_ai_memory_agent())
    asyncio.run(azure_open_ai_message_store_agent())

if __name__ == "__main__":
    main()