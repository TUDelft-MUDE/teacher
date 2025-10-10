# Assignment files

In MUDE, we have assignments in separate private repositories which we share with students via the workbook and/or GitHub Classroom. This page explains how to work in those repositories and prepare those.

## Prepare assignments
In MUDE we have three types of assignments (next to assignments in the book):
- Programming assignments, to be made individually, submitted via GitHub Classroom and graded automatically in a workflow
- Workshop assignments, to be made individually or in groups during our Wednesday session. Not submitted, not graded but solutions are provided after the session.
- Group assignments, to be made in groups during our Friday sessions, submitted via GitHub Classroom and graded manually. Solutions are not provided.

For each of these assignments a repository has been made in [the MUDE-2025 GitHub organization](https://github.com/MUDE-2025) and are initiated as explained below. Access to these repositories is restricted for teachers and TAs and can be requested for by mailing T.R.vanWoudenberg@tudelt.nl. Content leaders can add others to individual repositories as they like and can define their own way of collaboration, although it is generally advised to use a git-workflow with branches and pull-requests ([see this page, which describes how this is done for the MUDE Textbook)](book-edit_workflow)). Assignment repositories are set up differently from the Textbook, however: by default only the content leader have push and merge access to main (others can have the same permissions when given an admin role), and the branches of the git repository are set up in a special way to facilitate integration with GitHub Classroom (e.g., checking student submissions), as well as defining files with and without solutions (`solution` and `assignment` branches, each of which are generated from the `main` branch to ensure consistency). The easiest way to contribute to an assignment when you didn't receive access by a content leader (before it has been released to students!) is to create a fork of the repository, make your changes on the `main` branch, then submit a PR back to the `main` branch of the PA repository in the `MUDE-2025` organization (forking this repo will result in a private repo, so there is no concern about releasing solutions early). Note that while the changes should be made as commits to `main`, it may be easier to view the file contents on the `assignment` or `solution` branch, as that is what the students will interact with. Furthermore, never commit directly to the `assignment` or `solution` branch (you cannot do that) or create PRs to those branches. These branches are updated automatically and are only meant for viewing.

As soon an assignment is ready, ask the content coordinator for a review. If passed, the assignments is added by the content coordinator to the workbook which shows a preview of the assignments and allows students to download. For programming and group assignments, a [github classroom assignment is initiated too](./github-classroom.md).

To add the files to the workbook, the content coordinator updated the submodule in the workbook and adds the relevant files to the `_toc.yml`.

(formatting_assignments)=
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
