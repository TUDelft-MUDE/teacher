# %pip install PyGithub

from github import Github
from pathlib import Path

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

# Step 6: Add ipynb_template.ipynb to the repository
print("Adding ipynb_template.ipynb to the repository...")
with open("ipynb_template.ipynb", "r") as file:
    ipynb_template_content = file.read()
new_repo.create_file("ipynb_template.ipynb", "Add ipynb_template.ipynb", ipynb_template_content)
print("ipynb_template.ipynb has been added successfully.")

# Step 6.1: Add CITATION.cff file
print("Adding CITATION.cff...")
citation_file_path = Path("CITATION.cff")
citation_content = citation_file_path.read_text()
new_repo.create_file("CITATION.cff", "Add CITATION.cff", citation_content)

# Step 6.2: Add LICENSE file
print("Adding LICENSE file...")
license_file_path = Path("LICENSE")
license_content = license_file_path.read_text()
new_repo.create_file("LICENSE", "Add LICENSE file", license_content)

# Step 6.3: Add report_template.md file
print("Adding report_template.md...")
report_template_path = Path("report_template.md")
report_template_content = report_template_path.read_text()
new_repo.create_file("report_template.md", "Add report_template.md", report_template_content)

# Step 6.4: Add requirements.txt file
print("Adding requirements.txt...")
requirements_file_path = Path("requirements.txt")
requirements_content = requirements_file_path.read_text()
new_repo.create_file("requirements.txt", "Add requirements.txt", requirements_content)

# Step 6.6: Add generate-student-notebook.yml file
print("Adding generate-student-notebook.yml...")
workflow_dir = ".github/workflows"
workflow_file = "generate-student-notebook.yml"
workflow_file_path = Path(workflow_dir) / workflow_file
workflow_content = workflow_file_path.read_text()
new_repo.create_file(
    workflow_file,
    "Add generate-student-notebook.yml",
    workflow_content
)

# Step 6.5: move workflow file manually as the path with a dot is not allowed

print(f"Repository '{NEW_REPO_NAME}' created and configured successfully!")

# Step 7: Update repository settings
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