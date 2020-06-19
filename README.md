# Skill 'Em All

This is a course project for University of Helsinki course [Database application](https://materiaalit.github.io/tsoha-20/osa0/).

## Abstract

Skill 'Em All is an application for finding right people for the projects based on peoples skills. Lets say you are a manager of the project which has a requirement for Java and React knowledge. With Skill 'Em All you can search people with those skills and find out the best people for the project.

### Main features

- User can create an account
- User can login/logout
- User can view and manage profile
- User can add/update/remove skills
- User can search other users by skill
- User can create/close projects
- User can add users to her/his projects

## Skill 'Em All live

Latest build of this app is running on Heroku:

- [Skill 'Em All Heroku](https://skill-em-all.herokuapp.com/)

## Documentation

- [Database shema](https://github.com/MiguelSombrero/skill-em-all/tree/master/documentation/schema.md)

- [User stories and queries](https://github.com/MiguelSombrero/skill-em-all/tree/master/documentation/features.md)

- [Manual](https://github.com/MiguelSombrero/skill-em-all/tree/master/documentation/manual.md)

## Application requirements

You need to have `python` installed in order to run the app

## Install and run application locally

Clone the project and navigate to the application folder

    git clone https://github.com/MiguelSombrero/skill-em-all.git
    cd skill-em-all

Install project dependencies

    pip install -r requirements.txt

Run application

    python run.py

Application is listening address

    http://localhost:5000

## Deploy app to Heroku

You need to have [Heroku account](https://www.heroku.com/) account and [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) in order to deploy app to heroku with these instructions.

When in application root folder, create heroku app:

    heroku create <name-of-your-application>

Add heroku remote to your local git repository

    git remote add heroku <address-in-heroku-of-your-application>

Add required environment variables to Heroku

    heroku config:set HEROKU=1

Add Postgres database to your Heroku application

    heroku addons:add heroku-postgresql:hobby-dev

Commit and push your changes to heroku

    git add .
    git commit -m "deploy to Heroku"
    git push heroku master

## TODO

- exception handling
- paging in Find people view
- information if specific person is available (or tied into another project)
- do not show 'add to project' buttons in Find people view for projects user already in
- ... and lots of minor bug fixes and betterments