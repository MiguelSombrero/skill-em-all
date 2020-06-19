# User stories and queries

## User can create an account

### Queries

Account is queried by username to see if username is already taken

    SELECT *
    FROM Account
    WHERE username = 'username'
    LIMIT 1

If username is not taken, user is persisted in database

    INSERT INTO Account (name, username, password, email)
    VALUES ('name', 'username', 'password', 'email')

## User can delete account

### Queries

Account is deleted by query

    DELETE FROM Account
    WHERE id ='id'

And all the related data with cascading deletes

    DELETE FROM Project
    WHERE Project.id = ?

    DELETE FROM Skill
    WHERE Skill.id = ?
    
    DELETE FROM Experience
    WHERE Experience.id = ?

## User can login

### Queries

Account is queried by username to verify that username exists and password is correct. Query is identical to one made when creating an account.

## User can logout

## User can view and update profile

### Queries

Account is queried by id

    SELECT *
    FROM Account
    WHERE id = 'id'

Queried account is updated in the database

    UPDATE Account
    SET name = 'name', username = 'username', password = 'password', email = 'email', profile_info = 'profile_info'
    WHERE id = 'id'

## User can add skills

### Queries

Application checks whether you already have skill you about to save

    SELECT *
    FROM Skill
    WHERE name = 'name'
    AND owner_id = 'id'
    LIMIT 1

If this query doesn't return any values, skill is saved in db

    INSERT INTO Skill (name, account_id)
    VALUES ('name', 'account_id')

Also experiences related to this skill is saved to db. There can be more than one different experiences related to one skill

    INSERT INTO Experience (experience_type, experience, skill_id)
    VALUES ('type', 'experience', 'skill_id')

## User can view skills

### Queries

Account object is called with skills and experiences, when user loads skills page

    SELECT *
    FROM Account
    LEFT JOIN Skill ON Skill.owner_id = Account.id
    LEFT JOIN Experience ON Experience.skill_id = Skill.id
    WHERE Account.id = 'id'
    ORDER BY Experience.experience DESC

## User can update skill

### Queries

First skill is queried by id in order to check whether it is owned by logged user

    SELECT *
    FROM Skill
    LEFT JOIN Experience ON Experience.skill_id = Skill.id
    WHERE Skill.id = 'id'
    ORDER BY Experience.experience DESC

If it is, all experiences related to that skill is updated

    UPDATE Experience
    SET experience = 'experience'
    WHERE Experience.skill_id = 'skill_id'

## User can remove skills

### Queries

First skill is queried by id as in update skill user story. After that, skill and related experiences is deleted from db

    DELETE FROM skill
    WHERE skill.id = ?
    
    DELETE FROM experience
    WHERE experience.id = ?
    
## User can search other users by skill

When user searches other users, two queries are being made

### Queries

Current users active projects are fetched

    SELECT Project.id, Project.name
    FROM Project
    WHERE Project.owner_id = 'id'
    AND Project.active = 1

Accounts are fetched by skill name

    SELECT *
    FROM Account
    LEFT JOIN Skill ON Skill.owner_id = Account.id
    LEFT JOIN Experience ON Experience.skill_id = Skill.id
    WHERE Skill.name LIKE 'name'
    ORDER BY Experience.experience DESC

## User can create projects

### Queries

    INSERT INTO Project (name, start_date, end_date, owner_id)
    VALUES ('name', 'start_date', 'end_date', 'owner_id')

## User can close projects

### Queries

    UPDATE Project
    SET active = FALSE
    WHERE Project.id = 'id'

## User can view own projects

### Queries

Projects are queried by owner id. Account and Account_project tables are joined to find projects staff and staff count

    SELECT a.id, a.name, a.start_date, a.end_date, a.active, a.account_name, b.staff_count
    FROM (
        SELECT Project.*, Account.name AS account_name
        FROM Project
        LEFT JOIN Account_project ON Project.id = Account_project.project_id
        LEFT JOIN Account ON Account.id = Account_project.account_id
        WHERE Project.owner_id = ?
        GROUP BY Project.id, Account.name) a
        LEFT JOIN (
            SELECT project_id AS id, COUNT(*) AS staff_count
            FROM Account_project
            GROUP BY project_id) b ON a.id = b.id

## User can add other users to projects he/she owns

### Queries

Project is queried by id in order to check whether it is owned by logged user. If so, project id and account is is inserted into join table

    INSERT INTO account_project (account_id, project_id)
    VALUES ('account_id', 'project_id')