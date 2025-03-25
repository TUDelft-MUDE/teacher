# Textbook

We make use of an interactive online textbook to share content with students.Therefore, we make use of the [TeachBooks](https://teachbooks.tudelft.nl/) platform, which is a spin-off of [Jupyter Book](https://jupyterbook.org/en/stable/intro.html).

## Viewing the book

- Material is released to students when a commit is made to the `2025` branch at [https://mude.citg.tudelft.nl/book/2025](https://mude.citg.tudelft.nl/book/2025)
- Prior to sharing with students, material should be reviewed by making a commit to the `2025-draft` branch. This can be viewed at [https://mude.citg.tudelft.nl/book/2025-draft/](https://mude.citg.tudelft.nl/book/2025-draft/).
- All other branches are meant to be 'in development' and can be viewed on GitHub. Default is that the branch name is added after the root URL/repo_name. Actions page which summarizes all the branches and status: [https://github.com/TUDelft-MUDE/book/actions](https://github.com/TUDelft-MUDE/book/actions). As soon as the content is merged with the other content, these temporary branches are removed.


## Editing the book
Anyone with access can edit the book in the github repository: [https://github.com/TUDelft-MUDE/book](https://github.com/TUDelft-MUDE/book) with the following steps:
- Create a branch with your edits
- Open a draft pull request and ask for feedback from fellow content experts / TAs / content coordinator / programming coordinator.
- As soon as it ready, mark the pull request as ready and ask the content coordinator for a review (if you didn't do that before)
- The content coordinator will merge you pull request and delete your branch.

We identify a few user-types (taken from the [TeachBooks Manual](https://teachbooks.io/manual/installation-and-setup/user_types.html)), pecifically for this MUDE-book:
- User type 1/2: review by opening an issue by clicking the lightbulb on the top-right corner of a page.
- User type 3/4/5: edit a file on a new branch and create a merge request to 2025-draft as described above

Depending on the type of user you want to be, you need to know only a few details or a bit more. If you're completely new, go through the general introduction to these kind of books at platforms in the 'Your first TeachBook!' part of the  [TeachBooks Manual](https://teachbooks.io/manual/intro.html). If you already now the basic, go through  relevant pages (indicated per user type per page) in the `Getting going!` part of the manual.

The yearly and draft branches are protected with [a ruleset](./Protect_main.json). This is requiring pull requests for the with 1 approval (which hare dismissed upon new commits), requiring conversation resolution before merging, merging without rebase and blocking force pushes while allowing bypass by organization admins and the MUDE MT.

Starting in the academic year 2025-2026, we apply ['TeachBooks versioning with `academic_year.additions.errata`](https://teachbooks.io/manual/installation-and-setup/versioning_changelog.html). This is coordinated by the content coordinator.

## Exercises
For exercises in the book, we'd like to use:
- [interactive python code](https://teachbooks.io/manual/features/live_code.html)
- [interactive HTML/JavaScript elements](https://teachbooks.io/manual/features/HTML_javascript.html)
- [interactive H5p elements](https://teachbooks.io/manual/features/h5p.html). Ask for access to [shared folder](https://tudelft.h5p.com/content/1292046735045725667) at Tom van Woudenberg

## FTP storage
Images and binary or big files should be stored on our FTP-server. More information will follow soon.

## Attribution
````{margin}
```{attributiongrey} Attribution
:class: attribution
Written by Tom van Woudenberg
```
````

For every chapter, a note on attribution is added to make clear who are the authors. Therefore, use the following syntax (see example on the right sidebar):
`````md
````{margin}
```{attributiongrey} Attribution
:class: attribution
Written by <author(s)>
```
````
`````

Add this note to the main page of a chapter on top and to the bottom of each of the subpages.

If the page is taken from another book, add the following:

`````md
````{margin}
```{attributiongrey} Attribution
:class: attribution
Written by <author(s)>

This page reuses CC BY content from {cite:t}`<reference in book/_bibliography/references.bib>`. {fa}`quote-left`[Find out more here](external_resources)
```
````
`````

And add relevant external_recourses to `book/credits.md`. To make this possible we use the custom admonitions of [the custom named colors sphinx extension](https://teachbooks.io/manual/external/Sphinx-Named-Colors/README.html#admonitions) in combination with a [custom css file](./_static/attribution.css) in `book/_static/` and the line `named_colors_custom_colors: {'attributiongrey':[150,150,150]}` in `book/_config.yml` under `sphinx: config: `

## Copyright and Licenses
The book is released openly, copyrighted by all of us as employees from Delft University of Technology, with a CC BY License. Please comply to the obvious rules for citations for text and figures and don't use non-licensed (or non compatible with our CC BY license) material from others. Some content has been taken out of the book because of copyright risks in preparation for the 2025-2026 academic year. Read [the TeachBooks manual](https://teachbooks.io/manual/installation-and-setup/copyright.html) for more information about how to deal with copyright.

## Permissions GitHub
Permissions are managed with GitHub teams and organization roles:
- Teacher and TAs are added to the 'Content writers' team with an all-repository write role.
- The MUDE MT team has an all-repository admin role

If you don't have access to this repository, request for it by asking Tom (programming coordinator). If you want to start straight away, fork the book instead of creating a fork.

### A bit of history

- 2022-23: we made a Jupyter Book to archive of all material; students did not use an online book, only Brightspace
- 2023-24: we made our first Jupyter Book, which used the draft-release workflow to release material
- 2024-25: goal is to make the book open with a CC-BY license. GitHub (TeachBooks) is used to mirror the repo and facilitate a large number of draft versions of the book that can be used for review via the github actions workflow
- 2025-26: all the book stuff is moved to GitHub to ease the deployment flow.
