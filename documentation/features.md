# Features

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

**Note: is this correct according to how SQLAlchemy ORM works**

Account is deleted by query

    DELETE FROM Account
    WHERE id ='id'

## User can login

### Queries

Account is queried by username to verify that username exists and password is correct. Query is identical to one made when creating an account.

## User can logout

## User can view and update profile

### Queries

Account is queried by id

    SELECT *
    FROM Account
    WHERE id = 'id

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



## User can remove skills

### Queries

## User can search other users by skill

### Queries

## User can create projects

### Queries

## User can delete projects

### Queries

## User can view own projects

### Queries

## User can add other users to projects he/she owns

### Queries