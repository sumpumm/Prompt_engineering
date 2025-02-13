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
    role = "You are an expert in digital marketing."
    
    instruction = "I need you to help me create 10 Instagram hooks to generate sales of my product."
    
    context = "I am  selling an online service to help people better manage their health by eating healthy."
    
    example = """
        Here are some examples of hooks that have performed well:
        Fuel Your Body: Top Tips for a Balanced Diet!

        Healthy Eating Made Simple: Quick and Tasty Recipes!
        Boost Your Energy: Discover the Power of Clean Eating!
    """
    

    # role = input("Enter the role of the AI (e.g., You are an expert in marketing): ")
    # context = input("Enter the context (e.g., I am selling an online service for healthy eating): ")
    # example = input("Enter an example (e.g., 'Boost Your Energy: Discover the Power of Clean Eating!'): ")
    # instruction = input("\nInstruction: ")

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