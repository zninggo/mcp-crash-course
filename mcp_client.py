import asyncio
import os

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

from langchain_openai import ChatOpenAI

load_dotenv(override=True)

llm = ChatOpenAI(
    model=os.getenv('OPENAI_MODEL'),
    base_url=os.getenv('OPENAI_BASE_URL'),
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0.7
)

async def main():
    pass

if __name__ == "__main__":
    asyncio.run(main())