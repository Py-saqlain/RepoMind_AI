import git
import os
import shutil
import stat

def remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def clone_repo(repo_url: str) -> str:
    repo_name = repo_url.rstrip("/").split("/")[-1]
    clone_path = f"temp/{repo_name}"

    if os.path.exists(clone_path):
        shutil.rmtree(clone_path, onexc=remove_readonly)

    os.makedirs("temp", exist_ok=True)
    git.Repo.clone_from(repo_url, clone_path, depth=1)

    return clone_path