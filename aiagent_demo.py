import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat

os.environ[
    "OPENAI_API_KEY"] = "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"

async def main_single_agent():

    model_client = OpenAIChatCompletionClient(model="gpt-5")
    assistant = AssistantAgent(name="assistant", model_client=model_client)
    await Console(assistant.run_stream(task="What is 25 * 8?"))
    await model_client.close()

async def main_single_agent_multimodal():

    model_client = OpenAIChatCompletionClient(model="gpt-5")
    assistant = AssistantAgent(name="assistant", model_client=model_client)
    image = Image.from_file("C:\\Users\\wasif.kazmi\\Github\\AI\\Janet.jpg")
    multimodal_message = MultiModalMessage(
        content=["What do you see in this image?", image], source="user")
    await Console(assistant.run_stream(task=multimodal_message))
    await model_client.close()

async def main_round_robin_group_chat():

    model_client = OpenAIChatCompletionClient(model="gpt-5")

    agent1 = AssistantAgent(name="MathTeacher", model_client=model_client,
                             system_message="You are a math teacher. Explain concepts clearly and ask follow-up questions")

    agent2 = AssistantAgent(name="Student", model_client=model_client,
                             system_message="You are a curious student. Ask questions and show your thinking process")

    team = RoundRobinGroupChat(participants=[agent1, agent2],
                                termination_condition=MaxMessageTermination(max_messages=3))

    await Console(team.run_stream(task="Let's discuss what is multiplication and how it works"))
    await model_client.close()

asyncio.run(main_round_robin_group_chat())
