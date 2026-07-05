from fastapi import APIRouter, HTTPException
from backend.schemas import IngestRequest, IngestResponse
from backend.services.cloner import clone_repo
from backend.services.chunker import chunk_repo
from backend.services.embedder import embed_and_store

router = APIRouter()

@router.post("/ingest", response_model=IngestResponse)
def ingest(req: IngestRequest):
    try:
        repo_path = clone_repo(req.repo_url)
        chunks = chunk_repo(repo_path)
        total = embed_and_store(chunks, req.repo_url)
        return IngestResponse(message="Repo indexed successfully", chunks=total)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))