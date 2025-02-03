from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage,AIMessage

llm=ChatOllama(model="llama3",temperature=1)
chat_history=[]

def main(question):
    prompt_template=ChatPromptTemplate.from_messages([
        ("system","You are a helpful AI assistant. Follow user instaructions and answer accordingly."),
        MessagesPlaceholder("chat_history"),
        ("human","{input}"),
        ])

    chain= prompt_template | llm

    response=chain.invoke({"input": question,"chat_history":chat_history})

    chat_history.extend([
    HumanMessage(content=question),
    AIMessage(content=response.content)
    ])
    
    return response.content

