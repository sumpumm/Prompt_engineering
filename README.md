 ### AI-Powered Dynamic RICEQ Prompting System

This project aims to implement the RICEQ technnique of prompting. This project enables interactive conversations with an AI model using OpenRouter's API. The system dynamically refines user input by generating follow-up questions before providing the final response.

### Features:

- Dynamic Role Definition – Users can specify the AI's role (e.g., marketing expert, fitness coach).

- Context Awareness – Provides better responses based on user-defined context.

- Follow-up Questioning – The AI asks clarifying questions before generating output.

- Chat History Tracking – Maintains conversation context for accurate responses.

### Usage

Run the script and follow the prompts:

- python main.py

- Enter the AI's role, context, example, and instruction.

- The AI generates a follow-up question for clarification.

- Provide your response.

- The AI processes the conversation and outputs the final result.

### Example
Hardcode the paramaters instead of taking inputs like:
    role = "You are an experienced web developer with expertise in teaching HTML to beginners"
    instruction = """
    Write a simple HTML code example for students that demonstrates the basic structure of an HTML webpage. The code should include a heading, a paragraph, and a link. 
    Keep it clean, well-indented, and beginner-friendly.
    """
    context = """The students are new to HTML and learning how to structure a webpage. The goal is to provide a clear, 
    easy-to-understand example that introduces fundamental HTML elements.
    """
    example = """
        The code should follow a simple structure, such as:
        Using <h1> for the main heading
        Adding a <p> for a short description
        Including an <a> tag to link to an external website

    """
    

### Code Overview

- Imports dependencies and initializes chat history.

- Connects to OpenAI via OpenRouter API.

- Prompts user for role, context, example, and instruction.

- AI generates a follow-up question to refine the input.

- User responds, and chat history is updated.

- Final response is generated based on the full conversation.
