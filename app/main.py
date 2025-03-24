from dotenv import load_dotenv
from pydantic_ai import Agent
load_dotenv()

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent_1 = None
agent_2 = None
@app.get("/agent/{agent_name}")
async def run_code(agent_name: str):
    global agent_1, agent_2
    if agent_name == "agent_1":
        agent_1 = Agent(
            model="openai:gpt-4o-2024-11-20",
        )

        result = await agent_1.run("Generate a random number between 1 and 100")
        return result.data
    elif agent_name == "agent_2":
        agent_2 = Agent(
            model="google-vertex:gemini-1.5-pro",
        )

        result = await agent_2.run("Generate a random character between a and z")
        return result.data 
    else:
        raise HTTPException(status_code=400, detail="Invalid agent name")

