import os
import asyncio
from agent_framework.azure import AzureAIAgentClient
from azure.identity.aio import AzureCliCredential
from dotenv import load_dotenv

load_dotenv()

async def foundry_agent():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentClient(
            project_endpoint=os.getenv("PROJECT_ENDPOINT"),
            model_deployment_name=os.getenv("MODEL_DEPLOYMENT_NAME"),
            async_credential=credential,
            agent_name="HelperAgent"
        ).create_agent(
            instructions="You are a helpful assistant.") as agent,
    ):
        result = await agent.run("Hello!")
        print(result.text)

def main():
    asyncio.run(foundry_agent())

if __name__ == "__main__":
    main()