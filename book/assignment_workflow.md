# Assignment administration workflow

## Steps to publish assignments:
1. Update formatting files if not done yet:

    - Citation file
    - CC BY footer
    - Consistent headers
    - Catchy title in readme, descriptive title for files
    - Readme contains links with relative paths to the other files.
    - Binary files (images, datasets) are stored on FTP server or Git LFS repository.
    - No copyright issues
    - Split files into separate tasks where possible
    - Add markdown version of `.py` files (to be implemented in workflow) in `assignment_book` and `solution_book` branch.
    - Placeholders in `README.md` are replaced with the actual assignment name.

2. If programming assignment:

    - Change default branch of assignment repository to `assignment` (Settings - Branches - Default branch - Change default branch)
    - Create new assignment based on this template assignment with the same name but with `_template` after it (so for example `PA1.1_template`).

3. Check correct version in `.gitmodules` file: `assignment`.
4. Adjust `toc.yml` in workbook with all files of the assignment. The readme is taken as the section header page, the other files are added as subsections.
5. Update changelog in workbook
6. Add version tag to repository (locally, push changes)
7. Check whether automatic commits don't include undesired changes from other assignment repositories.
8. Check rendering in book
9. Update overview on homepage MUDE
10. Update changelog and tag for homepage
11. Share link with students

More details below

## Steps to update assignments with typos or solution:
1. Update assignment repository.
2. If solution to be published: change branch name in `.gitmodules` file to `solution`.
3. If assignment is finished:
    - Make assignment repository public
4. Update changelog in workbook
5. Add version tag to workbook repository (locally, push changes)
6. If no changes have been made to the workbook-repository, but you want to update the workbook with the updated assignment repositories: trigger the build workflow manually from [the workflow tab](https://github.com/TUDelft-MUDE/workbook-2026/actions/workflows/deploy-book.yml)
7. Check whether automatic commits don't include undesired changes from other assignment repositories.
8. Check rendering in book
9. If group assignment finished, start grading process

More details below.

Solutions are shared for/on:

- Workshop assignments after processing the feedback collected for the workshop, preferably on the same day.
- Group assignments after grading
- Programming assignments after deadline: preferable on Saturday after Friday deadline.

## Prepare repositories as administrator

1. Create an organization for your assignments. This repository will include source repositories, but also student repositories.
2. Go to {octicon}`person` `People` to add members. In MUDE, the MUDE MT is added to a team (under {octicon}`people` `Teams`) and has been given All-repository admin rights under {octicon}`gear` `Settings` - {octicon}`organization` `Organization roles` - `Role assignment`.
3. Apply for [a GitHub Education GitHub Team](https://education.github.com/globalcampus/teacher) for your organization to get unlimited workflow minutes in the GitHub classroom repos, allow adding many students to the organization at the same time and GitHub pages (public) for private repositories)
4. Create repositories from the template repsitory with the same git history: https://github.com/TUDelft-MUDE/assignment_repo_template. Therefore clone the template repository and push it to a new remote (it's like a fork, but you cannot create more than one fork). This template contains a `README.md` containing some basic information, a citation file, template notebook, license file, template report, requirements file and github workflow for stripping out assignment and solution blocks. In MUDE we use:
   - `WS1.1` for workshops assignments indicated with `<Q1/Q2>.<week1-8>`
   - `GA1.1` for group assignments indicated with `<Q1/Q2>.<week1-8>`
   - `PA1.1` for programming assignments indicated with `<Q1/Q2>.<week1-8>`
5. Go to {octicon}`gear` `Settings` - {octicon}`gear` General:
   - under `General`: check `Template repository`
   - under `Features`: uncheck `Wikis`
   - under `Pull requests`: check `Always suggest updating pull request branches Loading` and `Automatically delete head branches`
6. Go to {octicon}`repo-push` `Rules` - `Rulesets`, click `Import a ruleset` and import [this file](./protect_assignment_and_solution.json). This is imported to protect the `assignment` and `solution` branches which should be read-only.
7. Go to {octicon}`gear` `Settings` - {octicon}`people` `Collaborators and teams` to add the responsible people. In MUDE the responsible teacher of the topic has admin access and can add his topic-colleagues. To bypass this, a repository secret needs to be added to every repository called `FG_MUDE_2025_TOKEN`, which can be a fine-grained PAT with a least `content` access.

## Combine assignments in workbook
The workbook has all the assignment repos as [submodules](https://teachbooks.io/manual/external/Nested-Books/README.html) so that it can use those files to create previews in the book. To be able to clone those submodules during the build, a personal access token is added as `GH_PAT` to the repository action secrets with 'repo' scope, as explained [in the TeachBooks Manual](https://teachbooks.io/manual/external/deploy-book-workflow/README.html#private-submodules). Furthermore, a step in the [workflow](https://github.com/TUDelft-MUDE/workbook-2025/blob/release/.github/workflows/deploy-book.yml) is included to update submodules.

## Release assignment in workbook

How to release an assignment to students in the workbook is shown below (note that this video includes a deprecated implementation of github dependabot):

```{video} https://www.youtube.com/watch?v=ryhD623UqZ0
```

To share the solution, change the branch `assignment` to `solution` in the `.gitmodules` file and retrigger the dependabot as shown in shown in the video above (and merge pull request,update changelog and add version number)

Which should then be followed by the same steps as shown above to add the assignment to the workbook.

## Permissions GitHub

Permissions are managed with GitHub teams and organization roles:
- Teacher and TAs are added with an all-repository read role
- The MUDE MT team (child team of the 'Teacher and TAs'-team) has an all-repository admin role
- Child teams of the 'Teacher and TAs'-team are created for every topic. The content leaders are added to these teams. These teams are assigned admin rights for their specific assignment repositories, allowing them full control over their repositories (except for editing the assignment and solution branch).

The base permission of the organisation is set to 'no permissions', repository and pages creation is disabled ( {octicon}`gear` `Settings` - {octicon}`people` `Member privileges`). Furthermore, admin repository permissions are all disabled ( {octicon}`gear` `Settings` - {octicon}`people` `Collaborators and teams` - Admin repository permissions).
