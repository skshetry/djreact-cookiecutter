# Sambad
[![pipeline status](https://gitlab.com/DanglingPointers/djreact-boilerplate/badges/master/pipeline.svg)](https://gitlab.com/DanglingPointers/djreact-boilerplate/commits/master)
[![coverage report](https://gitlab.com/DanglingPointers/djreact-boilerplate/badges/master/coverage.svg)](https://gitlab.com/DanglingPointers/djreact-boilerplate/commits/master) 

This is an ambitious project for developing an enterprise communication tool that is focused on providing collaborative communication software and that is secure and isolated.

In heavy Development with Django and React with <3

## Installation instructions
1. Clone this repo, preferably using ssh clone instead of https,
 so that you won't be bothered for password everytime you push or pull.
    - `git clone git@gitlab.com:git@gitlab.com:DanglingPointers/djreact-boilerplate.git`
2. We use `postgresql` for database.  [Installation Guide](https://www.postgresql.org/download/)
    - Depending on the job, you may want to install [pgcli](https://github.com/dbcli/pgcli)
    or [pgadmin4](https://www.pgadmin.org/download/)(provides graphical ui).
    - Create database. Open `psql` (or, `pgcli`) and enter following sql query.
    ```sql
    CREATE DATABASE sambad
    ```
    > If you want other database name to be other than `sambad`, 
    > [you may need to add a environment variable of the database name](#custom-db-name))
3. `cd` into this repo(where you cloned it). You will see the following repo structure *roughly*.

        .
        ├── backend
        ├── .coverage
        ├── env.example
        ├── frontend
        ├── .git
        ├── .gitignore
        ├── .gitlab-ci.yml
        └── README.md
    - There's clear separation between backend and frontend.
    - Now create a virtual environment for python and activate. 
        - On shell, `python -m venv backend/venv`

            On Windows if above didn't work, `c:\Python36\python -m venv c:\path\to\venv`. ^[[1](https://docs.python.org/3/library/venv.html)]

        - Activate: `source backend/venv/bin/activate`

            On Windows, either use `backend\venv\Scripts\activate.bat` on `cmd.exe` or `backend\venv\Scripts\Activate.ps1`on `PowerShell`(default on Windows 10).

        - Test if it's working. `which python` should return the path having the current directory somewhere in the parent of the path.
    
4. Install all the requirements (`pip install -r backend/requirements/local.txt`).

5. Copy file `env.example` from root of this repo in a new file `.env`(dot env) in same directory.
    - `cp env.example .env`
        >Warning:  Don't delete `env.example` though.

6. Open the file and change `user` with database owner(usually the `username`) and `pass` with your database password(usually your user password).
    - <a name="custom-db-name"></a> If you have set the name of db other than `sambad`, you need to uncomment the `#POSTGRES_DBNAME` line and change the value to the db name.
7. `cd backend` if you are not already in.
8. Make migrations file and then migrate.
    - `python manage.py makemigrations`
    - `python manage.py migrate` 
    > Not working? Maybe you forgot to activate virtual environment?
9. Run test to ensure everything is working.
    - `python manage.py test`
    > Tests failed? It's likely that the setup didn't go well. Maybe, you skipped something. 
10. Change directory to `frontend` directory, from the root of the repo.

11. Install dependencies for frontend and run tests for verifying everything.
    - `npm install`
    - `npm test`

    > Tests fine? Congratulations. Now, the tedious setup has come to an end. 

12. Run `node` server.
    - `npm run start`

13. Run backend server from backend directory.
    - `python manage.py runserver`

14. Now, open [localhost:8000](http://localhost:8000).

    > Don't want to run two servers? Fine. 
    > Not recommended if you are working on frontend.
    >  You may lose out the perks that `node` provides.
    > - Build bundle using `npm build`.
    > - Uncomment the line `#DJANGO_BUILD_WEBPACK=True`
    > - Rerun the backend server(running node server not required as it's already built)
    > - Visit [localhost:8000](http://localhost:8000) as usual.

## Development
1. Create an issue before you start working on.
2. Create an `WIP` merge request and branch for working on that issue.
3. Only work on the issue and don't mix it with others.
4. At least one should review it before merging.
5. Be helpful on other's issues and suggest and discuss potential solutions.
6. Master should be auto-deployable, so code cannot be pushed in it. 
7. Pull that using `git pull --all` and checkout to the new branch(`git checkout <branchname>`).
