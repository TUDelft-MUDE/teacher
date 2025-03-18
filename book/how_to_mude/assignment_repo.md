# Prepare assignments on GitHub

In MUDE, we create assignments in separate private repositories which we share with students via a workbook and GitHub Classroom. This page explains how to create assignments

1. Create a organization for your assignments. This repository will include source repositories, but also student repositories.
2. Apply for [a GitHub Education GitHub Team](https://education.github.com/globalcampus/teacher) for your organization to get unlimited workflow minutes in the GitHub classroom repos, allow adding many students to the organization at the same time and GitHub pages (public) for private repositories)
3. Add a empty repository (if you already have a template repository, make it based on that template) and give it a logical name. In MUDE we use:
   - `WS1.1` for workshops assignments indicated with `<Q1/Q2>.<week1-8>`
   - `GA1.1` for group assignments indicated with `<Q1/Q2>.<week1-8>`
   - `PA1.1` for programming assignments indicated with `<Q1/Q2>.<week1-8>`
4. Add a `README.md` containing some basic information. In MUDE we start with for example:
```md
# Programming assignment 1.1

This repository contains source file for the assignment and will be used a source for student repositories and in the workbook.

> Copyright 2025 MUDE, Delft University of Technology. This work is licensed under a CC BY 4.0 License
```
5. Go to {octicon}`gear` `Settings` - {octicon}`gear` General:
   - under `General`: check `Template repository`
   - under `Features`: uncheck `Wikis`
   - under `Pull requests`: check `Always suggest updating pull request branches Loading` and `Automatically delete head branches`
6. Go to {octicon}`repo-push` `Rules` - `Rulesets`, click `Import a ruleset` and import [this file](./Protect%20main.json). This will require pull requests for the main branch with 1 approval, allowing bypass by organization admins
