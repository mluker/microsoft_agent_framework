import os
import asyncio
from agent_framework.azure import AzureOpenAIResponsesClient
from azure.identity import AzureCliCredential
from dotenv import load_dotenv

load_dotenv()

async def azure_open_ai_responses_agent():
    agent = AzureOpenAIResponsesClient(
        endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        deployment_name=os.getenv("MODEL_DEPLOYMENT_NAME"),
        api_version="preview",
        credential=AzureCliCredential()
    ).create_agent(
        instructions="You are good at telling jokes.",
        name="Joker"
    )

    result = await agent.run("Tell me a joke about a pirate.")
    print(result.text)

def main():
    asyncio.run(azure_open_ai_responses_agent())


if __name__ == "__main__":
    main()