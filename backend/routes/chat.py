from fastapi import APIRouter, HTTPException
from backend.schemas import ChatRequest, ChatResponse
from backend.services.rag import get_answer

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        answer = get_answer(req.repo_url, req.question)
        return ChatResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))