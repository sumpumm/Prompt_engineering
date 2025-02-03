from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

llm =  ChatGroq(
    model="mixtral-8x7b-32768",
    api_key=api_key,
    temperature=1
)

chat_history = []

def main(question):
    
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. Follow user instructions and answer accordingly."),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])

    chain = prompt_template | llm

    response = chain.invoke({"input": question, "chat_history": chat_history})

    chat_history.extend([
        HumanMessage(content=question),
        AIMessage(content=response.content)
    ])
    
    return response.content

 
