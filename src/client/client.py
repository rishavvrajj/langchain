from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client= MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["src/server/math.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http"
            }
        }
    )

    import os 
    os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

    tools=await client.get_tools()
    model= ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite",google_api_key=os.getenv("GOOGLE_API_KEY"))
    agent= create_agent(
        model,tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 x 4) x 12 ?"}]}
    )
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's the weather in california?"}]}
    )

    print("\n=== math response ===")
    math_response["messages"][-1].pretty_print()

    print("\n=== weather response ===")
    weather_response["messages"][-1].pretty_print()

asyncio.run(main())