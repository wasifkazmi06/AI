import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

os.environ[
    "OPENAI_API_KEY"] = "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"

async def main1():
    print( "I am inside function" )

    model_client = OpenAIChatCompletionClient(
        model="gpt-5" )
    assistant = AssistantAgent( name="assistant", model_client=model_client )
    await Console( assistant.run_stream( task="What is 25 * 8?" ) )
    await model_client.close()


asyncio.run( main1() )
