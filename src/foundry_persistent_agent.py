import os
import asyncio
from agent_framework.azure import AzureAIAgentClient
from azure.identity.aio import AzureCliCredential as AsyncAzureCliCredential
from azure.ai.projects.aio import AIProjectClient
from agent_framework import ChatAgent
from dotenv import load_dotenv

load_dotenv()

async def foundry_persistent_agent():
    async with (
        AsyncAzureCliCredential() as credential,
        AIProjectClient(
            endpoint=os.getenv("PROJECT_ENDPOINT"),
            credential=credential) as project_client,
    ):
        # Create a persistent agent
        created_agent = await project_client.agents.create_agent(
            model=os.getenv("MODEL_DEPLOYMENT_NAME"),
            name="PersistentAgent",
            instructions="You are a helpful assistant.")

        try:
            # Use the agent
            async with ChatAgent(chat_client=AzureAIAgentClient(project_client=project_client,
                                                                agent_id=created_agent.id),
                                                                instructions="You are a helpful assistant.") as agent:
                result = await agent.run("Hello!")
                print(result.text)
        finally:
            # Clean up the agent
            await project_client.agents.delete_agent(created_agent.id)

def main():
    asyncio.run(foundry_persistent_agent())

if __name__ == "__main__":
    main()