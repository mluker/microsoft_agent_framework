import os
import asyncio
from agent_framework.azure import AzureAIAgentClient
from azure.identity.aio import AzureCliCredential as AsyncAzureCliCredential
from dotenv import load_dotenv

load_dotenv()

async def foundry_streaming_agent():
    async with (
        AsyncAzureCliCredential() as credential,
        AzureAIAgentClient(async_credential=credential,
                           project_endpoint=os.getenv("PROJECT_ENDPOINT"),
                           model_deployment_name=os.getenv("MODEL_DEPLOYMENT_NAME"),
                           )
        .create_agent(name="StreamingAgent", instructions="You are a helpful assistant.") as agent,
    ):
        print("Agent: ", end="", flush=True)
        async for chunk in agent.run_stream("Tell me a short story"):
            if chunk.text:
                print(chunk.text, end="", flush=True)
        print()

def main():
    asyncio.run(foundry_streaming_agent())

if __name__ == "__main__":
    main()