 ### AI-Powered Dynamic RICEQ Prompting System

This project aims to implement the RICEQ technnique of prompting. This project enables interactive conversations with an AI model using OpenRouter's API. The system dynamically refines user input by generating follow-up questions before providing the final response.

### Features:

- Dynamic Role Definition – Users can specify the AI's role (e.g., marketing expert, fitness coach).

- Context Awareness – Provides better responses based on user-defined context.

- Follow-up Questioning – The AI asks clarifying questions before generating output.

- Chat History Tracking – Maintains conversation context for accurate responses.

### Usage

This code is designed to only run once. In each run, when you prompt the LLM it asks you a followup question and when you asnwer it, you'll recieve the final output. Run the script and follow the prompts:

- python main.py

- Enter the AI's role, context, example, and instruction.

- The AI generates a follow-up question for clarification.

- Provide your response.

- The AI processes the conversation and outputs the final result.

### Example
- Consider the following hardcoded prompt
  ![prompt](https://github.com/user-attachments/assets/7c30b939-6731-463b-a043-948da1871a83)
- The LLM asks you a followup question
 ![fo,llow](https://github.com/user-attachments/assets/079e5d67-e139-43fd-ac07-67c751b0a2b1)
- The final output
  ![output](https://github.com/user-attachments/assets/aaaffb40-7950-4ada-a73b-1acff0e4f9dc)

### Code Overview

- Imports dependencies and initializes chat history.

- Connects to OpenAI via OpenRouter API.

- Prompts user for role, context, example, and instruction.

- AI generates a follow-up question to refine the input.

- User responds, and chat history is updated.

- Final response is generated based on the full conversation.
