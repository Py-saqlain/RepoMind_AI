import os
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

FAISS_INDEX_DIR = "indexes"

def get_index_path(repo_url: str) -> str:
    repo_name = repo_url.rstrip("/").split("/")[-1]
    return os.path.join(FAISS_INDEX_DIR, repo_name)

def embed_and_store(chunks: list[Document], repo_url: str) -> int:
    embeddings = FastEmbedEmbeddings()
    index_path = get_index_path(repo_url)
    os.makedirs(FAISS_INDEX_DIR, exist_ok=True)
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(index_path)
    return len(chunks)