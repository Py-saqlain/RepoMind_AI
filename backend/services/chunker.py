from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from backend.services.filter import filter_files

MAX_FILES = 100
MAX_FILE_SIZE = 30000  # ~30KB per file, skips huge generated/minified files

def chunk_repo(repo_path: str) -> list[Document]:
    files = filter_files(repo_path)
    files = files[:MAX_FILES]
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    all_chunks = []

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            if not content.strip() or len(content) > MAX_FILE_SIZE:
                continue
            chunks = splitter.create_documents(
                texts=[content],
                metadatas=[{"source": file_path}]
            )
            all_chunks.extend(chunks)
        except Exception:
            continue

    return all_chunks