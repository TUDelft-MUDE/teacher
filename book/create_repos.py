# %pip install PyGithub

from github import Github

# Replace these with your details
GITHUB_TOKEN = "PASTE_HERE"
ORG_NAME = "MUDE-2025"
NEW_REPO_NAME = "WS2.8"  # Example: Programming Assignment 1.1

# Authenticate with GitHub
g = Github(GITHUB_TOKEN)
org = g.get_organization(ORG_NAME)

# Step 4: Create a new empty repository
print(f"Creating new empty repository '{NEW_REPO_NAME}'...")
new_repo = org.create_repo(
    name=NEW_REPO_NAME,
    private=True,
    has_issues=True,
    has_projects=False,
    has_wiki=False,
)

# Step 5: Add a README.md file
print("Adding README.md...")
readme_content = """# Workshop assignment 2.8

This repository contains source file for the assignment and will be used a source for student repositories and in the workbook.

> Copyright 2025 MUDE, Delft University of Technology. This work is licensed under a CC BY 4.0 License
"""
new_repo.create_file("README.md", "Add README.md", readme_content)

# Step 6: Update repository settings
print("Updating repository settings...")
new_repo.edit(
    is_template=True  # Mark as a template repository
)
new_repo.edit(
    delete_branch_on_merge=True  # Automatically delete head branches
)
new_repo.edit(
    allow_update_branch=True  # Always suggest updating pull request branches
)


print(f"Repository '{NEW_REPO_NAME}' created and configured successfully!")