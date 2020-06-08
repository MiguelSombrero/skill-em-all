# Manual

## Create an account

User can create an account by clicking link `Register` from the navigation bar and filling information in registration form. Name, username and password is mandatory fields, providing email is optional. After succesfull registration, user is redirected to login page.

## Login

User can login by clicking link `Login` from the navigation bar and filling username and password in login form.

## Logout

After user is logged in, user can logout by clicking link `Logout` from the navigation bar.

## View, update or delete profile

User can view his/hers profile by clicking the link `Me -> My Profile` from navigation bar. In profile page, user can update name, profile info, password and email. If password is not given, application won't update password. Username cannot be changed.

User can delete account clicking `Delete account` button. This will also delete all skills and projects related to that profile.

## View and add skills

User can view, add and delete skills by clicking the link `Add skills` from navigation bar and filling skill form. Skill can be any skill or knowledge, which you would use in your CV - for example 'Python' or 'Agile methods'. 

## View, update and delete skills

User can view, update and delete skills by clicking the link `Me -> My Skills` from navigation bar.  

## Create project

User can create projects by clicking the link `Create project` from navigation bar and filling project form. After succesfully creating a project, user is redirected to projects page.

## View projects

User can view projects by clicking the link `Me -> My projects` from navigation bar. Projects page shows current users all *active* projects (e.g. projects which is not closed).

## View and close project

User can view project by going projects page (clicking the link `Me -> My projects` from navigation bar) and selecting a project (Manage project link). Project page shows basic information about the project, including people already attached to this project, and summary about skills and experiences in this project.

User can close project by clicking `Close project`button. *This does not delete project* from the database, it only sets the `Project.active` attribute to false.

## Search other users by skill

User can search other users by clicking link `Find people` from the navigation bar, or giving skill name in the search bar directly. Leave search box empty to list all users.

## Add users to projects

User can add other users to his/hers projects form `Find people` view, by clicking button with projects name, in left side column. After succesfull addition, user is redirected to project page.
