import asyncio
import json
import os

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat, SelectorGroupChat
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_ext.tools.mcp import StdioServerParams, mcp_server_tools

os.environ[
    "OPENAI_API_KEY"] = "dummyKey"

async def single_agent():

    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
    assistant = AssistantAgent(name="assistant", model_client=model_client)
    await Console(assistant.run_stream(task="What is 25 * 8?"))
    await model_client.close()

async def single_multimodal_agent():

    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
    assistant = AssistantAgent(name="assistant", model_client=model_client)
    image = Image.from_file("C:\\Users\\wasif.kazmi\\Github\\AI\\Janet.jpg")
    multimodal_message = MultiModalMessage(
        content=["What do you see in this image?", image], source="user")
    await Console(assistant.run_stream(task=multimodal_message))
    await model_client.close()

async def round_robin_group_chat_agent():

    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
    agent1 = AssistantAgent(name="MathTeacher", model_client=model_client,
                             system_message="You are a math teacher. Explain concepts clearly and ask follow-up questions")
    agent2 = AssistantAgent(name="Student", model_client=model_client,
                             system_message="You are a curious student. Ask questions and show your thinking process")
    team = RoundRobinGroupChat(participants=[agent1, agent2],
                                termination_condition=MaxMessageTermination(max_messages=3))
    await Console(team.run_stream(task="Let's discuss what is multiplication and how it works"))
    await model_client.close()

async def human_agent():

    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
    assistant = AssistantAgent(name="MathTutor", model_client=model_client,
                                system_message="You are helpful math tutor. Help the user solve math problems step by step. When the user says 'THANKS DONE' or similar, acknowledge and say 'LESSON COMPLETE' to end session.")
    user_proxy = UserProxyAgent(name="Student")
    team = RoundRobinGroupChat(participants=[user_proxy, assistant], termination_condition=TextMentionTermination("LESSON COMPLETE"))
    await Console(team.run_stream(task = "I need help with algebra problem"))

async def state_saved_agent():

    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
    agent1 = AssistantAgent(name="Helper", model_client=model_client)
    agent2 = AssistantAgent(name="BackupHelper", model_client=model_client)
    await Console(agent1.run_stream(task="My favourite color is green because it reminds me of nature."))
    state = await agent1.save_state()
    with open("memory.json", "w") as f:
        json.dump(state, f, default=str)
    with open("memory.json", "r") as f:
      saved_state = json.load(f)
    await agent2.load_state(saved_state)
    await Console(agent2.run_stream(task="What is my favourite color?"))
    await model_client.close()

async def selector_group_chat_agent():

    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
    researcher = AssistantAgent(
        "ResearcherAgent",
        model_client=model_client,
        system_message="You are a researcher. Your role is to gather information and provide research findings ONLY. Do not write articles or create content - just provide research data and facts.")
    writer = AssistantAgent(
        "WriterAgent",
        model_client=model_client,
        system_message="You are a writer. Your role is to take research information and create well-written articles. Wait for research to be provided, then write the content.")
    critic = AssistantAgent(
        "CriticAgent",
        model_client=model_client,
        system_message="You are a critic. Review written content and provide feedback. Say 'TERMINATE' when satisfied with the final result.")
    text_termination = TextMentionTermination("TERMINATE")
    max_messages_termination = MaxMessageTermination(max_messages=10)
    termination = text_termination |max_messages_termination
    team = SelectorGroupChat(participants=[critic, writer, researcher],
                       model_client=model_client, termination_condition=termination,
                       allow_repeated_speaker=True)
    await Console(team.run_stream(task ="Research on who is a better ODI batsman between Virat Kohli and Steve Smith, write an article on it, and provide critique on the article."))
    await model_client.close()

async def web_surfer_agent():

    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
    web_agent = MultimodalWebSurfer(
        name="WebSurfer",
        model_client=model_client,
        headless= False,
        animate_actions=True)
    agent_team = RoundRobinGroupChat(participants=[web_agent], max_turns=2)
    await Console(agent_team.run_stream(task="Find the schedule of Indian cricket team till 2026 and list out the matches and venues. Save or print it as a table."))
    await web_agent.close()
    await model_client.close()

async def mcp_server_tool_agent():
    
    filesystem_server_params = StdioServerParams(command="npx",
                                                  args=[
                                                        "-y", 
                                                        "@modelcontextprotocol/server-filesystem",
                                                        "C:\\Users\\wasif.kazmi"
                                                        ],
                                                  read_timeout_seconds=60)
    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    # Get tools from the workbench
    tools = await mcp_server_tools(filesystem_server_params)
    math_tutor = AssistantAgent(name="MathTutor", model_client=model_client, tools=tools,
                                    system_message="You are helpful math tutor. Help the user solve math problems step by step. You have access to file system tools. When the user says 'THANKS DONE' or similar, acknowledge and say 'LESSON COMPLETE' to end session.")
    user_proxy = UserProxyAgent(name="Student")
    team = RoundRobinGroupChat(participants=[user_proxy, math_tutor],
        termination_condition=TextMentionTermination("LESSON COMPLETE"))
    await Console(team.run_stream(task="I need help with algebra problem. Tutor, feel free to create files to help with student learning"))

    await model_client.close()

asyncio.run(mcp_server_tool_agent())

