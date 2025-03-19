# Prepare assignments on GitHub

In MUDE, we create assignments in separate private repositories which we share with students via the workbook and/or GitHub Classroom. This page explains how to create assignment repositories.

1. Create a organization for your assignments. This repository will include source repositories, but also student repositories.
2. Go to {octicon}`person` `People` to add members. In MUDE, the MUDE MT is added to a team (under {octicon}`people` `Teams`) and has been given All-repository admin rights under {octicon}`gear` `Settings` - {octicon}`organization` `Organization roles` - `Role assignment`.
3. Apply for [a GitHub Education GitHub Team](https://education.github.com/globalcampus/teacher) for your organization to get unlimited workflow minutes in the GitHub classroom repos, allow adding many students to the organization at the same time and GitHub pages (public) for private repositories)
4. Add a empty repository (if you already have a template repository, you can make it based on that template) and give it a logical name. In MUDE we use:
   - `WS1.1` for workshops assignments indicated with `<Q1/Q2>.<week1-8>`
   - `GA1.1` for group assignments indicated with `<Q1/Q2>.<week1-8>`
   - `PA1.1` for programming assignments indicated with `<Q1/Q2>.<week1-8>`
5. Add a `README.md` containing some basic information. In MUDE we start with for example:
```md
# Programming assignment 1.1

This repository contains source file for the assignment and will be used a source for student repositories and in the workbook.

> Copyright 2025 MUDE, Delft University of Technology. This work is licensed under a CC BY 4.0 License
```
6. Go to {octicon}`gear` `Settings` - {octicon}`gear` General:
   - under `General`: check `Template repository`
   - under `Features`: uncheck `Wikis`
   - under `Pull requests`: check `Always suggest updating pull request branches Loading` and `Automatically delete head branches`
7. Go to {octicon}`repo-push` `Rules` - `Rulesets`, click `Import a ruleset` and import [this file](./Protect_main.json). This will require pull requests for the main branch with 1 approval, allowing bypass by organization and repo admins
8. Go to {octicon}`gear` `Settings` - {octicon}`people` `Collaborators and teams` to add the responsible people. In MUDE the responsible teacher of the topic has admin access and can add his topic-colleagues.

Step 4 - 6 have been implemented in a [script](./_static/create_repos.ipynb) for MUDE-2025. For this you need a GitHub Token. My Personal access token (classic) has `repo` permissions.