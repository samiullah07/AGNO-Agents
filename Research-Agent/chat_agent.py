from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools import tool
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

# @tool
# def brave_search(query: str):
#     """Search the internet using DuckDuckGo."""
#     with DDGS() as ddgs:
#         results = ddgs.text(query, max_results=5)
#         return [r["body"] for r in results]
    


agent = Agent(
    name ="Research Agent",
    description ="""
Always run the search tool first for the query.

Return 3–5 relevant links with titles and URLs.

Summarize findings in concise bullet-point format with inline sources.

""",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[DuckDuckGoTools()    ]


)


agent.print_response("Research three recent articles about Agentic AI, list titles + links and then summarize them")