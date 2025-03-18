# Interactive Online Textbooks

We make use of an interactive online textbook to share content with students.Therefore, we make use of the [TeachBooks](https://teachbooks.tudelft.nl/) platform, which is a spin-off of [Jupyter Book](https://jupyterbook.org/en/stable/intro.html).

## Viewing the book

- Material is released to students when a commit is made to the `2025` branch at [https://mude.citg.tudelft.nl/book/2025](https://mude.citg.tudelft.nl/book/2025)
- Prior to sharing with students, material should be reviewed by making a commit to the `2025-draft` branch. This can be viewed at [https://mude.citg.tudelft.nl/book/2025-draft/](https://mude.citg.tudelft.nl/book/2025-draft/).
- All other branches can be viewed on GitHub. Default is that the branch name is added after the root URL/repo_name. Actions page which summarizes all the branches and status: [https://github.com/TUDelft-MUDE/book/actions](https://github.com/TUDelft-MUDE/book/actions)


## Editing the book
You can edit the book in the gitlab repository: [https://github.com/TUDelft-MUDE/book](https://github.com/TUDelft-MUDE/book). If you don't have access, request for it by asking Tom.

Depending on the type of user you want to be, you need to know only a few details or a bit more. Find out which user type you want to be at [https://teachbooks.tudelft.nl/jupyter-book-manual/installation-and-setup/user_types.html](https://teachbooks.tudelft.nl/jupyter-book-manual/installation-and-setup/user_types.html).

Specifically for this MUDE-book:
- User type 1/2: review by opening an issue by clicking the lightbulb on the top-right corner of a page
- User type 3/4/5: edit a file on a new branch and create a merge request to 2025-draft. Request for a merge by asking the content manager (Robert/Jialei).

If you've never edited a book before, go through the relevant pages (indicated per user type per page) in the `Your first TeachBooks` part of the [TeachBooks Manual](https://teachbooks.io/manual/intro.html) first.


## Tags

- `2023-archive`
- `2023-archive-2`: Hypothesis was removed, so the `-x` numbering scheme was implemented
- `2024-v0` only to id start point. not going to use other `v` numbers


### A bit of history

- 2022-23: we made a Jupyter Book to archive of all material; students did not use an online book, only Brightspace
- 2023-24: we made our first Jupyter Book, which used the draft-release workflow to release material
- 2024-25: goal is to make the book open with a CC-BY license. GitHub (TeachBooks) is used to mirror the repo and facilitate a large number of draft versions of the book that can be used for review via the github actions workflow
- 2025-26: all the book stuff is moved to GitHub to ease the deployment flow.