# Assignment files

In MUDE, we have assignments in separate private repositories which we share with students via the workbook and/or GitHub Classroom. This page explains how to work in those repositories and prepare those.

## Prepare assignments
In MUDE we have three types of assignments (next to assignments in the book):
- Programming assignments, to be made individually, submitted via GitHub Classroom and graded automatically in a workflow
- Workshop assignments, to be made individually or in groups during our Wednesday session. Not submitted, not graded but solutions are provided after the session.
- Group assignments, to be made in groups during our Friday sessions, submitted via GitHub Classroom and graded manually. Solutions are not provided.

For each of these assignments a repository has been made in [the MUDE-2025 GitHub organization](https://github.com/MUDE-2025) and are initiated as explained below. Content leaders can add others as they like and can define their own way of collaboration (although it's advised to use [a git-workflow with branches and pull-request as there is for the book](book-edit_workflow)). By default only the content leader have push and merge access to main, others can have the same permissions when given an admin role.

As soon an assignment is ready, ask the content coordinator for a review. If passed, the assignments is added by the content coordinator to the workbook which shows a preview of the assignments and allows students to download. For programming and group assignments, a [github classroom assignment is initiated too](./github-classroom.md).

To add the files to the workbook, the content coordinator updated the submodule in the workbook and adds the relevant files to the `_toc.yml`.

## Formatting assignments
Assignments should be formatted in such a way that they're readable on:
- local machines (raw markdown, notebooks enhanced with HTML)
- GitHub (raw markdown, notebooks enhanced with HTML)
- Jupyterbook (raw markdown, notebooks enhanced with HTML and evantually with MyST)

To do this, all of the assignment repositories include a template notebook, template readme and template report (as included in this [zip](./repo_template.zip)).

### Assignment and solution version
An assignment and solution version is created for all the markdown and notebook files when pushing to the main branch (using [the workflow file included in repo_template](./repo_template.zip)). Therefore, the main branch should include all information.

Based on the cell tags `solution` and `assignment`, and html solution blocks (recognized by color) parts of the notebook are stripped out:
- An assignment notebook is created by stripping out solution code cells (indication with cell tag `solution`) and cells with solution html boxes.
- A solution notebook created by stripping out assignment code cells (indicated with cell tag `assignment`) and runs the notebooks. The workflow will give a warning if the run doesn't succeed.

For markdown documents, two version are created based on comments:
```md
% solution_start
...
% solution_end
```
- An assignment markdown document is created by stripping out everything between the comments `% solution_start` and `%solution_end` including the comments itself.
- A solution markdown document is created by stripping just the comments `% solution_start` and `%solution_end`.

An `assignment` and `solution` branch are created / updated with all files in the repository including the stripped notebooks and markdown documents. These branches are protected and cannot be edited.

## FTP storage
Images and binary or big files should be stored on our FTP-server. More information is available [here](./FTP.md)

## Licensing

The assignments are shared with a CC BY license. During the academic year, the source code is hidden and only shared with students via the workbook and github classroom. When the academic year ends, the workbook-repository will be made public. The embedded assignments are converted from a submodule relation to the raw files.

## Prepare repositories as administrator

1. Create an organization for your assignments. This repository will include source repositories, but also student repositories.
2. Go to {octicon}`person` `People` to add members. In MUDE, the MUDE MT is added to a team (under {octicon}`people` `Teams`) and has been given All-repository admin rights under {octicon}`gear` `Settings` - {octicon}`organization` `Organization roles` - `Role assignment`.
3. Apply for [a GitHub Education GitHub Team](https://education.github.com/globalcampus/teacher) for your organization to get unlimited workflow minutes in the GitHub classroom repos, allow adding many students to the organization at the same time and GitHub pages (public) for private repositories)
4. Add a empty repository (if you already have a template repository, you can make it based on that template) and give it a logical name. In MUDE we use:
   - `WS1.1` for workshops assignments indicated with `<Q1/Q2>.<week1-8>`
   - `GA1.1` for group assignments indicated with `<Q1/Q2>.<week1-8>`
   - `PA1.1` for programming assignments indicated with `<Q1/Q2>.<week1-8>`
5. Add a `README.md` containing some basic information. And add a citation file, template notebook, license file, template report, readme requirements file and github workflow for stripping out assignment and solution blocks. All of these files are combined in a [zip](./repo_template.zip) including a py script to upload each of these [here](./create_repos.py). Note that you need to move the workflow file manually as the script doesn't allow adding files with a dot.
6. Go to {octicon}`gear` `Settings` - {octicon}`gear` General:
   - under `General`: check `Template repository`
   - under `Features`: uncheck `Wikis`
   - under `Pull requests`: check `Always suggest updating pull request branches Loading` and `Automatically delete head branches`
7. Go to {octicon}`repo-push` `Rules` - `Rulesets`, click `Import a ruleset` and import [this file](./Protect_main.json). This is requiring pull requests for the default branch with 1 approval (which hare dismissed upon new commits), requiring conversation resolution before merging, merging without rebase, protecting the default branch and blocking force pushes while allowing bypass by organization and repo admins. Furthermore, [another ruleset](./protect_assignment_and_solution.json) is imported to protect the `assignment` and `solution` branches.
8. Go to {octicon}`gear` `Settings` - {octicon}`people` `Collaborators and teams` to add the responsible people. In MUDE the responsible teacher of the topic has admin access and can add his topic-colleagues. To bypass this, a repository secret needs to be added to every repository called `FG_MUDE_2025_TOKEN`, which can be a fine-grained PAT with a least `content` access.

Step 4 - 6 have been implemented in a [py script included in the zip](./create_repos.py) for MUDE-2025. For this you need a GitHub Token. My Personal access token (classic) has `repo` permissions.

## Combine assignments in workbook
The workbook has all the assignment repos as [submodules](https://teachbooks.io/manual/external/Nested-Books/README.html) so that it can use those files to create previews in the book. To be able to clone those submodules during the build, a personal access token is added as `GH_PAT` to the repository action secrets with 'repo' scope, as explained [in the TeachBooks Manual](https://teachbooks.io/manual/external/deploy-book-workflow/README.html#private-submodules). Furthermore, a [`.github/dependabot.yml`](https://teachbooks.io/manual/external/Nested-Books/README.html#the-external-book-is-updated) was added to allow automatic updates:

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

## Permissions GitHub

Permissions are managed with GitHub teams and organization roles:
- Teacher and TAs are added with an all-repository read role
- The MUDE MT team (child team of the 'Teacher and TAs'-team) has an all-repository admin role
- Child teams of the 'Teacher and TAs'-team are created for every topic. The content leaders are added to these teams. These teams are assigned admin rights for their specific assignment repositories, allowing them full control over their repositories.

The base permission of the organisation is set to 'no permissions', repository and pages creation is disabled ( {octicon}`gear` `Settings` - {octicon}`people` `Member privileges`). Furthermore, admin repository permissions are all disabled ( {octicon}`gear` `Settings` - {octicon}`people` `Collaborators and teams` - Admin repository permissions).

