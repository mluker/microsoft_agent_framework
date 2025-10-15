import os
import asyncio
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential
from dotenv import load_dotenv

load_dotenv()

async def azure_open_ai_chat_agent():
    credential = AzureCliCredential()
    async with AzureOpenAIChatClient(
        credential=credential,
        endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        deployment_name=os.getenv("MODEL_DEPLOYMENT_NAME")
    ).create_agent(
        instructions="You are good at telling jokes.",
        name="Joker"
    ) as agent:
        result = await agent.run("Tell me a joke about a pirate.")
        print(result.text)

def main():
    asyncio.run(azure_open_ai_chat_agent())

if __name__ == "__main__":
    main()
