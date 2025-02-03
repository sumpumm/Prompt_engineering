from pydantic import BaseModel,Field

class Query_input(BaseModel):
    prompt: str 
    
class Query_output(BaseModel):
    response: str

class PromptRequest(BaseModel):
    prompt: str