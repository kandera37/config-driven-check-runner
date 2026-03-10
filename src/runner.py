import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

SCANNER_PATH = os.getenv('SECRET_SCANNER_PATH')


def run_instance(instance: dict) -> None:
    instance_name = instance.get("name")
    repo = instance.get("repo_path")
    check = instance.get("check")
    output_path = instance.get("output_file")
    commits = instance.get("commits")
    print(
        f"Running {instance_name}\n"
        f"Repo path: {repo}\n"
        f"Check type: {check}\n"
        f"Output path: {output_path}\n"
        f"Commits: {commits}\n"
    )
    if check == "secret_scan":
        print("Preparing secret scanner run...")
        run_secret_scan(repo, commits, output_path)
    else:
        print(f"Unsupported check type: {check}")

def run_secret_scan(repo: str, commits: int, output_path: str):
    if not SCANNER_PATH:
        raise RuntimeError("SECRET_SCANNER_PATH is not set")
    command = [
        "python3",
        SCANNER_PATH,
        "--repo",
        repo,
        "--n",
        str(commits),
        "--out",
        output_path,
    ]
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )
        print (result.stdout)
        if result.stderr:
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to run secret scan: {repo}\n{e.stderr}")

