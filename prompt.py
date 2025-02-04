from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder


def conditional_prompt(role=None):
    if role is not None:
        prompt_template = """
        {role}
        {instruction}
        {context}
        {example}
        {question}
        """
        return ChatPromptTemplate.from_messages([
        ("system",prompt_template),
        MessagesPlaceholder("chat_history")
        ])
    else:
        prompt_template="""
        Instruction: {instruction}
        """

        return ChatPromptTemplate.from_messages([
        ("system",prompt_template),
        MessagesPlaceholder("chat_history")
        ])
    
    
    
    
