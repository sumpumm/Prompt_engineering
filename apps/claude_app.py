from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
llm = ChatAnthropic(model="claude-3-sonnet-20240229",anthropic_api_key=api_key)

prompt_template="""
    You are a helpful AI assistant. Follow user instructions and answer accordingly.
    
    Role: {role}
    
    Instruction: {instruction}
    
    Context: {context}
    
    Example: {example}
    
    Question: Before you begin, ask me a few questions that you think will help you create the best output possible.
"""

chat_history = []

def main(question):
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", prompt_template),
        MessagesPlaceholder("chat_history"),  # Ensures chat history persists
        ("human", "{input}"),
    ])

    chain = prompt_template | llm

    response = chain.invoke({"input": question, "chat_history": chat_history})

    chat_history.extend([
    HumanMessage(content=question),
    AIMessage(content=response.content)
    ])

    return response.content


print(main("How can I improve my diet?"))
print(main("Give me a meal plan for a week."))
