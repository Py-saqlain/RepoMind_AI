from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.ingest import router as ingest_router
from backend.routes.chat import router as chat_router

app = FastAPI(title="RepoMind AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "RepoMind AI is running"}