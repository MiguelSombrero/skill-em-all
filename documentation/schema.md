# Database schema

## Entity relation model

![Database shema](https://github.com/MiguelSombrero/skill-em-all/blob/master/documentation/skill_schema.jpg)

## Create database queries

    CREATE TABLE account (
	    id INTEGER NOT NULL, 
	    created DATETIME, 
	    name VARCHAR(64) NOT NULL, 
	    username VARCHAR(64) NOT NULL, 
	    password VARCHAR(256) NOT NULL, 
	    email VARCHAR(64), 
	    profile_info VARCHAR(500), 
	    PRIMARY KEY (id), 
	    UNIQUE (username)
    )

    CREATE TABLE skill (
	    id INTEGER NOT NULL, 
	    created DATETIME, 
	    name VARCHAR(64) NOT NULL, 
	    owner_id INTEGER NOT NULL, 
	    PRIMARY KEY (id), 
	    FOREIGN KEY(owner_id) REFERENCES account (id)
    )

    CREATE TABLE project (
	    id INTEGER NOT NULL, 
	    created DATETIME, 
	    name VARCHAR(64) NOT NULL, 
	    start_date DATE, 
	    end_date DATE, 
	    active INTEGER NOT NULL, 
	    owner_id INTEGER NOT NULL, 
	    PRIMARY KEY (id), 
	    FOREIGN KEY(owner_id) REFERENCES account (id)
    )

    CREATE TABLE account_project (
	    account_id INTEGER NOT NULL, 
	    project_id INTEGER NOT NULL, 
	    PRIMARY KEY (account_id, project_id), 
	    FOREIGN KEY(account_id) REFERENCES account (id) ON DELETE cascade, 
	    FOREIGN KEY(project_id) REFERENCES project (id) ON DELETE cascade
    )

    CREATE TABLE experience (
	    id INTEGER NOT NULL, 
	    created DATETIME, 
	    skill_id INTEGER NOT NULL, 
	    experience_type VARCHAR(64) NOT NULL, 
	    experience INTEGER NOT NULL, 
	    PRIMARY KEY (id), 
	    FOREIGN KEY(skill_id) REFERENCES skill (id)
    )

