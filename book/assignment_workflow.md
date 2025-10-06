# Assignment administration workflow

## Steps to publish assignments:
1. Prepare `toc.yml` in workbook with all files of the assignment with to be published files in `#START REMOVE-FROM-PUBLISH` en `#END REMOVE-FROM-PUBLISH` gates. The readme is taken as the section header page, the other files are added as subsections. Eventually, .py files can be added as well as subsections of the other files.
2. Update formatting files if not done yet:
    - Citation file
    - CC BY footer
    - Consistent headers
    - Catchy title in readme, descriptive title for files
    - Readme contains links with relative paths to the other files.
    - Binary files (images, datasets) are stored on FTP server
    - No copyright issues
    - Split files into separate tasks where possible
3. If GH classroom assignment:

    - Change default branch of assignment repository to `assignment` (Settings - Branches - Default branch - Change default branch)
    - Make new assignment in GH classroom based on the assignment repository
    - Change default branch back to `main`.
    - Create GH classroom assignment:
        - Set hard cutoff date
        - Private repositories
        - No admin access
        - No github codespaces
        - Protect file paths of tests and classroom workflow
    - Add GH classroom link to readme of assignment repository

4. Update changelog in workbook
5. Add version tag to repository (locally, push changes)
6. Sync changes by running dependabot under Github - Insights - Dependency graph - Dependabot - "Check for updates". Wait for pull request and merge.
7. Check rendering in draft book
8. Update overview on homepage MUDE
9. Update changelog and tag for homepage
10. Share link (including GH classroom link if provided) with students

More details below

## Steps to update assignments with typos or solution:
1. Update assignment repository
2. If solution to be published: change branch name in `.gitmodules` file. Eventually add new solution-`.py`-files which were not included before.
3. Sync changes by running dependabot under Github - Insights - Dependency graph - Dependabot - "Check for updates". Wait for pull request and merge.
4. Make assignment repository public
5. Update changelog in workbook
6. Add version tag to repository (locally, push changes)
7. if GH classroom assignment:
    - Set cutoff date a few minutes in the future
    - Make assignment inactive

More details below

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
7. Go to {octicon}`repo-push` `Rules` - `Rulesets`, click `Import a ruleset` and import [this file](./protect_assignment_and_solution.json). This is imported to protect the `assignment` and `solution` branches which should be read-only.
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

## Release assignment in workbook

How to release an assignment to students in the workbook is shown below:

```{video} https://www.youtube.com/watch?v=ryhD623UqZ0
```

To share the solution, change the branch `assignment` to `solution` in the `.gitmodules` file and retrigger the dependabot as shown in shown in the video above (and merge pull request,update changelog and add version number)

To release an assignment via github classroom, the workflow is shown below:

```{video} https://youtu.be/dph6VI3f-Qo
```

Which should then be followed by the same steps as shown above to add the assignment to the workbook.

## Permissions GitHub

Permissions are managed with GitHub teams and organization roles:
- Teacher and TAs are added with an all-repository read role
- The MUDE MT team (child team of the 'Teacher and TAs'-team) has an all-repository admin role
- Child teams of the 'Teacher and TAs'-team are created for every topic. The content leaders are added to these teams. These teams are assigned admin rights for their specific assignment repositories, allowing them full control over their repositories (except for editing the assignment and solution branch).

The base permission of the organisation is set to 'no permissions', repository and pages creation is disabled ( {octicon}`gear` `Settings` - {octicon}`people` `Member privileges`). Furthermore, admin repository permissions are all disabled ( {octicon}`gear` `Settings` - {octicon}`people` `Collaborators and teams` - Admin repository permissions).
