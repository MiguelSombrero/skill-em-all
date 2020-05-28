# Skill 'Em All

**Under development**

This is a course project for University of Helsinki course [Database application](https://materiaalit.github.io/tsoha-20/osa0/).

## Abstract

Skill 'Em All is an application for finding right people for the projects based on peoples skills. Lets say you are a manager of the project which has a requirement for Java and React knowledge. With Skill 'Em All you can search people with those skills and find out the best people for the project.

### Main features

- User can create an account
- User can view and manage profile
- User can add/remove skills
- User can search other users by skill
- User can create projects
- User can add other users to projects he/she manages

## Skill 'Em All live

Latest build of this app is running on Heroku:

- [Skill 'Em All Heroku](https://skill-em-all.herokuapp.com/)

## Documentation

- [Database shema](https://github.com/MiguelSombrero/skill-em-all/tree/master/documentation/schema.md)

- [Features in detail](https://github.com/MiguelSombrero/skill-em-all/tree/master/documentation/features.md)

- [Manual](https://github.com/MiguelSombrero/skill-em-all/tree/master/documentation/manual.md)


## Application requirements

Application requires python3 to run

## Install instructions

### Install locally

Clone the project and navigate to the application folder

    git clone https://github.com/MiguelSombrero/skill-em-all.git
    cd skill-em-all

Install project dependencies

    pip install -r requirements.txt

Run application

    python run.py

Application is listening address

    http://localhost:5000

### Deploy to Heroku



## TODO

- exception handling in views
- information is specific person available (tied into another project or not)
- etc etc