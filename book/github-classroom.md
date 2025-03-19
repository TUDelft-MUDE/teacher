# GitHub Classroom

_This is a work in progress. We will try to describe some of these things and more (mostly just giving insight, tips and a links, as most of the topics are well-described on github website anyway):_

1. what and how to set up a classroom and assignment
2. setting up some assignments
3. access, permission, etc
4. getting students access and assigning groups
5. using workflows to autograde (with examples)
6. github API to extract information (grading)

## Creating an Assignment

Once the assignment is created, a link is generated with the following form:

```
https://classroom.github.com/a/xxxxxxxx
```

where `xxxxxxxx` is an 8-character alphanumeric code for your assignment.

Clicking this link allows students to accept the assignment after identifying themselves (for this we upload a csv with all the student IDs). This will then create a new GitHub repository that is a fork of the original assignment repository.

### Overview of Repositories

In the end, there are at least three GitHub repositories for every assignment:

1. The original repository you use to create the assignment, which must be a template repository. See [](./assignment_repo.md) on how these are created. Aas long as it is private, even if in the same organization as the students, they will never see the this repo or its history if the Base permission is set to `No permission` (Organization - {octicon}`gear` `Settings` - {octicon}`people` `Member Privileges` - `Base permissions` - `No permission`.).
2. A new repository created in the GitHub Organization to which the GitHub Classroom is assigned. All student repositories will be forked from this one. Updates made to this repository can be synced with the student repositories (although this didn't seem to work with many student repositories)
3. A repository for the student, which is created when they click the link described above.

## Creating Groups
Students are able to create groups themselves. To predefine groups, you've to mimic that process:
1. Create a dummy assignment with new category group names
2. Open dummy assignment from invitation link 
3. skip student id selection
4. Create a new team with the desired group name
5. in another tab, go to Teams on GitHub and remove yourself from the team you just created
6. Go back to the GH classroom tab, and go back one page where you created the team, and refresh.
7. Now add a new team and repeat steps 5-6 until you have successfully created all teams.
