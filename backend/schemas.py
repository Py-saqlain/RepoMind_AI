from pydantic import BaseModel

class IngestRequest(BaseModel):
    repo_url: str

class ChatRequest(BaseModel):
    repo_url: str
    question: str

class IngestResponse(BaseModel):
    message: str
    chunks: int

class ChatResponse(BaseModel):
    answer: str