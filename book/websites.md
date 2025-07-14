# Websites

There are four key websites used for MUDE (from a student perspective):
- **Brightspace**: containing announcement, course information, buddy check and grades
- **homepage** [(`mude.citg.tudelft.nl/`)](https://mude.citg.tudelft.nl/): an interactive book serving as a landing page for students (of this year and previous years) and teachers (both active and external)
- **textbook** [(`mude.citg.tudelft.nl/book/2025`)](https://mude.citg.tudelft.nl/book/2025): an interactive book containing course content
- **workbook** [(`mude.citg.tudelft.nl/workbook-2025`)](https://mude.citg.tudelft.nl/workbook-2025) an interactive book containing assignments (in 2022-23 it was called `course-files`, in 2023-2025 it was called `files`)

The websites listed above have a special configuration that automatically redirects to a URL containing the current academic year (`.YYYY/`) and provides draft pages for teachers for the textbook and workbook. This is explained in a separate subsection below.

In addition, additional websites are built and maintained for specific purposes:
- **published textbook** [(`mude.citg.tudelft.nl/book/2024`)](https://mude.citg.tudelft.nl/book/2024): the most-recent complete textbook to showcase the content of MUDE.
- **incoming** [(`mude.citg.tudelft.nl/incoming`)](https://mude.citg.tudelft.nl/incoming): information for incoming students
- **teacher** [(`mude.citg.tudelft.nl/teacher`)](https://mude.citg.tudelft.nl/teacher): information for teachers teaching MUDE or others who want to copy (parts of) MUDE. Furthermore, this serves as a documentation page for ourselves.

The websites listed above are not set up for archiving (no redirect or URL with the year) and do not have draft pages.

## Draft websites

As the **textbook** and **workbook** pages an essential and important function in MUDE, they have special treatment for URL’s. There is a draft version of each site [`mude.citg.tudelft.nl/book/2025`](https://mude.citg.tudelft.nl/book/2025) and [`mude.citg.tudelft.nl/book/2025-draft`](https://mude.citg.tudelft.nl/book/2025-draft), and [`mude.citg.tudelft.nl/workbook-2025`](https://mude.citg.tudelft.nl/workbook-2025) and [`mude.citg.tudelft.nl/workbook-2025/draft`](https://mude.citg.tudelft.nl/workbook-2025/draft) (try it!). A banner is added to the top of these pages to help you recognize that you are on a draft website (not files).

This works via the [TeachBooks deploy workflow](https://teachbooks.tudelft.nl/jupyter-book-manual/features/custom_toc.html): changes to the `draft` branch update the draft sites and changes to the `current_year`/`release` branch update the student versions. This students version excludes pages which are commented our in the table of contents configuration file. All of this happens automatically with a commit or merge request in the respective GitHub repositories. This is referred to as the _draft-release workflow.

The URL setup that contains the year (`./YYYY/`) and alternative `draft` address ensures that: 1) material from previous years is always available to students in the future, and 2) teachers can stage and preview online material before releasing it to students. In addition, it means that "archiving" material each year requires minimal effort: 1) create new branches in the book repository and a new workbook repository 2) change the URL redirect (this should happen each year on August 1), and 3) update the [Archive page](https://mude.citg.tudelft.nl/).


## Permissions GitHub
Permissions to the GitHub-based source code are managed with GitHub teams and organization roles:
- Teacher and TAs are added to the 'Content writers' team with an all-repository write role.
- The MUDE MT team has an all-repository admin role
- The content leader is codeowner for the book and workbook, and the MUDE MT for the other websites. A review is required from them for a merge into the versions shared with students

<!-- **BELOW THIS IS WORK IN PROGRESS**

## Behavior, URL structure

When using links to an archived site (website, book, files), the following behavior is possible:
- Accessing this year’s files: `mude.citg.tudelft.nl/<website>/` redirects to `mude.citg.tudelft.nl/YYYY/<we-bsite>/`, keeping `YYYY visible in the URL
- Each year, teachers and students should make links to pages using the year, e.g., `mude.citg.tudelft.nl/2024/files/weekly_subdir/my_file.ext`
- When a website is archived, links to material from year YYYY will still go to pages from that year
- It is easy to work in "Teacher mode” by simply adding `teacher` to URL: `mude.citg.tudelft.nl/teacher/2024/files/weekly_subdir/my_file.ext`

## How are the websites built?

A pipeline has rule for each branch and can apply those rules when a specified event happens on each branch; in our cases we typically use merge and/or push as the trigger.
-->
