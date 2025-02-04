from pydantic import BaseModel,Field

class Query_input(BaseModel):
    role:str | None = None
    instruction: str | None = None
    context: str | None = None
    example: str | None = None
    question: str | None = None
    
class Query_output(BaseModel):
    response: str

class PromptRequest(BaseModel):
    prompt: str