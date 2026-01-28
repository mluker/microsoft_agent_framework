import os
import asyncio
from typing import Annotated
from agent_framework.azure import AzureOpenAIChatClient
from agent_framework import ai_function
from azure.identity import AzureCliCredential
from dotenv import load_dotenv
from pydantic import Field

load_dotenv()


@ai_function(name="weather_tool", description="Retrieves weather information for any location")
def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    return f"The weather in {location} is cloudy with a high of 15°C."


async def azure_open_ai_tools_agent():
    credential = AzureCliCredential()
    async with AzureOpenAIChatClient(
        credential=credential,
        endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        deployment_name=os.getenv("MODEL_DEPLOYMENT_NAME")
    ).create_agent(
        instructions="You are a helpful assistant",
        tools=get_weather
    ) as agent:
        result = await agent.run("What is the weather like in Amsterdam?")
        print(result.text)

def main():
    asyncio.run(azure_open_ai_tools_agent())


if __name__ == "__main__":
    main()
