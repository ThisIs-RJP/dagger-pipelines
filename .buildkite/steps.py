import os

repo_name = os.environ["REPO_NAME"]
branch = os.environ["BRANCH"]

print(f"repo={repo_name} branch={branch} FROM THE MAIN PIPELINE!!")
