import os

IGNORE_EXTENSIONS = [".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico",
                     ".pdf", ".zip", ".exe", ".lock", ".pyc"]

IGNORE_FOLDERS = ["node_modules", "__pycache__", ".git", ".venv", 
                  "venv", "dist", "build", ".idea", ".vscode"]

IGNORE_FILES = ["package-lock.json", "yarn.lock", "poetry.lock",
                "Pipfile.lock", ".env", ".env.example"]

def filter_files(repo_path: str) -> list[str]:
    valid_files = []

    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]

        for file in files:
            if file in IGNORE_FILES:
                continue
            ext = os.path.splitext(file)[1]
            if ext in IGNORE_EXTENSIONS:
                continue
            valid_files.append(os.path.join(root, file))

    return valid_files