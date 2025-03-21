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
7. Go to {octicon}`repo-push` `Rules` - `Rulesets`, click `Import a ruleset` and import [this file](./Protect_main.json). This is requiring pull requests for the default branch with 1 approval (which hare dismissed upon new commits), requiring conversation resolution before merging, merging without rebase, protecting the default branch and blocking force pushes while allowing bypass by organization and repo admins
8. Go to {octicon}`gear` `Settings` - {octicon}`people` `Collaborators and teams` to add the responsible people. In MUDE the responsible teacher of the topic has admin access and can add his topic-colleagues.

Step 4 - 6 have been implemented in a [script](./create_repos.py) for MUDE-2025. For this you need a GitHub Token. My Personal access token (classic) has `repo` permissions.

## Combine assignments in workbook
The assignments repos in MUDE (stored in [](https://github.com/MUDE-2025)) are combined in a workbook which shows a preview of the assignments and allows students to download. This workbook is stored in the [general MUDE organization](https://github.com/TUDelft-MUDE/workbook-2025) so that it can be published as a TeachBook on the same domain [](https://mude.citg.tudelft.nl/workbook-2025). This workbook has all the assignment repos as [submodules](https://teachbooks.io/manual/external/Nested-Books/README.html) so that it can use those files to create previews in the book. To be able to clone those submodules during the build, a personal access token is added as `GH_PAT` to the repository action secrets with 'repo' scope, as explained [in the TeachBooks Manual](https://teachbooks.io/manual/external/deploy-book-workflow/README.html#private-submodules). Furthermore, a [`.github/dependabot.yml`](https://teachbooks.io/manual/external/Nested-Books/README.html#the-external-book-is-updated) was added to allow automatic updates:

```yaml
version: 2
registries:
  submodule1-registry:
    type: "git"
    url: https://github.com/
    username: x-access-token
    password: ${{secrets.GH_PAT}}
    
updates:
  - package-ecosystem: "gitsubmodule" # See documentation for possible values
    directory: "/" # Location of package manifests
    schedule:
      interval: "monthly"
      day: "sunday"
      time: "23:59"
    registries:
      - submodule1-registry
```

The same `GH_PAT` is added to the repository dependabot secrets to allow access to the assignment repositories.

## Formatting assignments
Assignments should be formatted in such a way that they're readable on:
- local machines (raw markdown, can be enhanced with HTML)
- GitHub (raw markdown, can be enhanced differently with HTML)
- Jupyterbook (raw markdown, can be enhanced with myst and differently with HTML)

How is to be decided.

## Permissions GitHub

Permissions are managed with GitHub teams and organization roles:
- Teacher and TAs are added with an all-repository read role
- The MUDE MT team (child team of the 'Teacher and TAs'-team) has an all-repository admin role
- Child teams of the 'Teacher and TAs'-team are created for every topic. The content leaders are added to these teams. These teams are assigned admin rights for their specific assignment repositories, allowing them full control over their repositories.

The base permission of the organisation is set to 'no permissions', repository and pages creation is disabled ( {octicon}`gear` `Settings` - {octicon}`people` `Member privileges`). Furthermore, admin repository permissions are all disabled ( {octicon}`gear` `Settings` - {octicon}`people` `Collaborators and teams` - Admin repository permissions).