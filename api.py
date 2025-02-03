from fastapi import FastAPI, Form
from models import *
from ollama_app import main as ollama_main
# from claude_app import main as claude_main
from groq_app import main as groq_main

app = FastAPI()

@app.post("/chat/ollama", response_model=Query_output)
async def ollama_endpoint(query_input: Query_input):
    question = query_input.prompt
    response = ollama_main(question)
    return Query_output(response=response)


# @app.post("/chat/claude", response_model=Query_output)
# async def claude_endpoint(query_input: Query_input):
#     question = query_input.prompt
#     response = claude_main(question)
#     return Query_output(response=response)


@app.post("/chat/groq", response_model=Query_output)
async def groq_endpoint(query_input: Query_input):  # Renamed to groq_endpoint
    question = query_input.prompt
    response = groq_main(question)
    return Query_output(response=response)


@app.post("/process_prompt")
async def process_prompt(prompt: str = Form(..., description="MultiLinePrompt")):
    return { "prompt": prompt}
