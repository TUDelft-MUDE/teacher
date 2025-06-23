# Textbook

We make use of an interactive online textbook to share content with students.Therefore, we make use of the [TeachBooks](https://teachbooks.tudelft.nl/) platform, which is a spin-off of [Jupyter Book](https://jupyterbook.org/en/stable/intro.html).

## Viewing the book

- Material is released to students when a commit is made to the `2025` branch at [https://mude.citg.tudelft.nl/book/2025](https://mude.citg.tudelft.nl/book/2025)
- Prior to sharing with students, material should be reviewed by making a commit to the `2025-draft` branch. This can be viewed at [https://mude.citg.tudelft.nl/book/2025-draft/](https://mude.citg.tudelft.nl/book/2025-draft/).
- All other branches are meant to be 'in development' and can be viewed on GitHub. Default is that the branch name is added after the root URL/repo_name. Actions page which summarizes all the branches and status: [https://github.com/TUDelft-MUDE/book/actions](https://github.com/TUDelft-MUDE/book/actions). As soon as the content is merged with the other content, these temporary branches are removed.

(book-edit_workflow)=
## Editing the book
Anyone with access can edit the book in the github repository: [https://github.com/TUDelft-MUDE/book](https://github.com/TUDelft-MUDE/book) with the following steps:
- Create a branch with your edits and open a draft pull request. Eventually name issues which this pull request might solve.
- Ask for feedback from fellow content experts / TAs / content coordinator / programming coordinator.
- As soon as it ready, mark the pull request as ready and ask the content coordinator for a merge.
- The content coordinator will merge you pull request and delete your branch.

We identify a few user-types (taken from the [TeachBooks Manual](https://teachbooks.io/manual/installation-and-setup/user_types.html)), specifically for this MUDE-book:
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
Images and binary or big files should be stored on our FTP-server. More information is available [here](./FTP.md). If you add an image using MyST syntax, add the FTP link like this:

````md
```{figure} https://files.mude.citg.tudelft.nl/<filename>
---
name: figure_label
---
caption
```
````

If you'd like to use the [download link replacer](https://teachbooks.io/manual/external/Download-Link-Replacer/README.html) to add a button to download custom files, add those files to the FTP-server too:

````md
```{custom_download_link} https://files.mude.citg.tudelft.nl/<path to file>
:text: "Custom text"
:replace_default: "False"
```
````

Are you looking for any old images that were deleted? Take a look at the repository on the tag [images_archive](https://github.com/TUDelft-MUDE/book/tree/images_archive).

## Attribution
````{margin}
```{attributiongrey} Attribution
:class: attribution
Written by Tom van Woudenberg
```
````

```{attributiongrey} Attribution
:class: attribution
Written by <author(s)>
```

For every chapter, a note on attribution is added to make clear who are the authors. Add this note on independent pages on full-width. For chapters with multiple pages: add the note to the main page of a chapter on top in the margin. On the bottom of each of the subpages, we add the same attribution, but on the full width:

`````md
```{attributiongrey} Attribution
:class: attribution
Written by <author(s)>
```
`````

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

More information about these attribution blocks can be found in the [TeachBooks manual](https://teachbooks.io/manual/installation-and-setup/copyright/recommendations.html#format-as-custom-admonition)

## Copyright and Licenses
The book is released openly, copyrighted by all of us as employees from Delft University of Technology, with a CC BY License. Please comply to the obvious rules for citations for text and figures and don't use non-licensed (or non compatible with our CC BY license) material from others. Some content has been taken out of the book because of copyright risks in preparation for the 2025-2026 academic year. Read [the TeachBooks manual](https://teachbooks.io/manual/installation-and-setup/copyright.html) for more information about how to deal with copyright.

## Permissions GitHub
Permissions are managed with GitHub teams and organization roles:
- Teacher and TAs are added to the 'Content writers' team with an all-repository write role.
- The MUDE MT team has an all-repository admin role

If you don't have access to this repository, request for it by asking Tom (programming coordinator). If you want to start straight away, fork the book instead of creating a fork.

### A bit of history

- 2022-23: we made one Jupyter Book for a small part of MUDE (weeks 2.7 and 2.8) used by students (everything else was on Brightspace), then a second book to archive all material (not used by students; the 2022 archive is password protected because it contains some student work).
- 2023-24: we made our first Jupyter Book, which used (and pioneered) the draft-release workflow to release material and Sphinx Thebe interactive Python pages. Experience in MUDE inspires the creation of TeachBooks in Spring 2024.
- 2024-25: this will be the first version of the book to be released with a CC-BY license. GitHub (TeachBooks) was used to mirror the repo and facilitate a large number of draft versions of the book that can be used for review via the github actions workflow.
- 2025-26: all the book stuff is moved to GitHub to ease the deployment workflow (prior versions of the book used GitLab).
