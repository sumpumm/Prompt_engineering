from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage,AIMessage

llm=ChatOllama(model="llama3",temperature=1)
chat_history=[]

def main(role=None,instruction=None,context=None,example=None,question=None):
    prompt_template="""
    You are a helpful AI assistant. Follow user instructions and answer accordingly.
    
    Role: {role}
    
    Instruction: {instruction}
    
    Context: {context}
    
    Example: {example}
    
    Question: {question}
    """
    prompt_template=ChatPromptTemplate.from_messages([
        ("system",prompt_template),
        MessagesPlaceholder("chat_history")
        ])

    chain= prompt_template | llm

    response=chain.invoke({"role": role,"instruction":instruction,"context":context,"example":example,"question":question,"chat_history":chat_history})

    chat_history.extend([
    HumanMessage(content=instruction),
    AIMessage(content=response.content)
    ])
    
    return response.content

# role="You are an expert in digital marketing."
# instruction="I need you to help me create 10 Instagram hooks to generate sales of my product."
# context="I selling an online service to help people better manage their health by eating healthy."
# example="""Here are some examples of hooks that have performed well:
# Fuel Your Body: Top Tips for a Balanced Diet!

# Healthy Eating Made Simple: Quick and Tasty Recipes!
# Boost Your Energy: Discover the Power of Clean Eating!"""

# question="""Before you begin, ask me a few questions that you think will help you create the best output possible."""


# print(main(instruction=instruction))