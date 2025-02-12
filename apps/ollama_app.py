from openai import OpenAI
from langchain_core.messages import HumanMessage,AIMessage
chat_history = []

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)
def ask_llm(prompt):
    """ Sends a message to the LLM and returns its response """
    completion = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct:free",
        messages=[{"role": "user", "content": prompt}]
    )
    response = completion.choices[0].message.content
    return response

def main():
    role = input("Enter the role of the AI (e.g., You are an expert in marketing): ")
    context = input("Enter the context (e.g., I am selling an online service for healthy eating): ")
    example = input("Enter an example (e.g., 'Boost Your Energy: Discover the Power of Clean Eating!'): ")
    instruction = input("\nInstruction: ")

    follow_up_question = ask_llm(
        f"role: {role}\n\n"
        f"nstruction: {instruction}\n\n"
        f"Context: {context}\n\n"
        f"Example: {example}\n\n"
        f"Before proceeding, ask the user any necessary questions to create the best possible output.") # the prompt follows RICEQ technique
    
    print("\n LLM Follow-Up Question:", follow_up_question)
    
    follow_up_answer = input("\nYour Answer: ")
    
    chat_history.extend([HumanMessage(content=instruction), AIMessage(content=follow_up_answer)])

    final_output = ask_llm(
        f"User Instruction: {instruction}\n\n"
        f"chat history:{chat_history}")
    print("\nLLM Final Output:", final_output)

main()
