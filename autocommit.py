# import os
# import datetime
# from github import Github # Ensure you have PyGithub installed: pip install PyGithub, path updated

# # Get GitHub token from environment variable
# GITHUB_TOKEN = os.environ["GH_TOKEN"]
# REPO_NAME = os.environ["REPO_NAME"]  # e.g., "username/repo"
# FILE_PATH = "autocommit_log.txt"

# def main():
#     # Initialize GitHub API client
#     g = Github(GITHUB_TOKEN)
#     repo = g.get_repo(REPO_NAME)
    
#     # Get current timestamp
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     commit_message = f"Auto-commit: {timestamp}"
    
#     try:
#         # Get the file contents (if it exists)
#         contents = repo.get_contents(FILE_PATH)
#         new_content = contents.decoded_content.decode() + f"\n{timestamp}"
#         # Update the file
#         repo.update_file(
#             FILE_PATH,
#             commit_message,
#             new_content,
#             contents.sha
#         )
#     except:
#         # If file doesn't exist, create it
#         repo.create_file(
#             FILE_PATH,
#             commit_message,
#             timestamp
#         )

# if __name__ == "__main__":
#     main()