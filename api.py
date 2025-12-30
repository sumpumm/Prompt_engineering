from fastapi import FastAPI,Form
from models import *
from langchain_ollama import OllamaLLM
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,AIMessage
from prompt import conditional_prompt
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

app = FastAPI()

chat_history=[]

@app.post("/chat/ollama",response_model=Query_output)
async def ollama_endpoint(query_input: Query_input):
    llm=OllamaLLM(model="llama3",temperature=1)
    global chat_history
    role=query_input.role
    instruction = query_input.instruction
    context=query_input.context
    example=query_input.example
    question=query_input.question
    
    prompt_template =conditional_prompt(role=role)
    formatted_prompt = prompt_template.format_messages(
        role=role,
        instruction=instruction,
        context=context,
        example=example,
        question=question,
        chat_history=chat_history
    )

    response = llm.invoke(formatted_prompt)
    
    chat_history.append(HumanMessage(content=instruction))
    chat_history.append(AIMessage(content=response))
    return Query_output(response=response)


@app.post("/chat/groq", response_model=Query_output)
async def groq_endpoint(query_input: Query_input): 
    llm =  ChatGroq(
    model="mixtral-8x7b-32768",
    api_key=api_key,
    max_retries=5,
    temperature=1
    ) 
    global chat_history
    role=query_input.role
    instruction = query_input.instruction
    context=query_input.context
    example=query_input.example
    question=query_input.question
    
    prompt_template =conditional_prompt(role=role)
    formatted_prompt = prompt_template.format_messages(
        role=role,
        instruction=instruction,
        context=context,
        example=example,
        question=question,
        chat_history=chat_history
    )
    response = llm.invoke(formatted_prompt)
    
    chat_history.append(HumanMessage(content=instruction))
    chat_history.append(AIMessage(content=response.content))
    return Query_output(response=response.content)

@app.post("/proccess_example")
async def convert_example_json(example: str = Form()):
    return {"formatted_example": example}