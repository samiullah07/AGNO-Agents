from fastapi import FastAPI
from pydantic import BaseModel
from chat_agent import agent

app = FastAPI()
class QueryRequest(BaseModel):
    query: str
class QueryResponse(BaseModel):
    response: str

@app.post("/research", response_model=QueryResponse)
async def research(request: QueryRequest):
    response = agent.run(request.query)
    # Safely access possible attributes on the agent result; try common names then fall back to stringified response.
    text = getattr(response, "output_text", None) or getattr(response, "output", None) or str(response)

    return QueryResponse(response=text)