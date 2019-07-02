## Favority


A tool to keep tab on your daily favorite things
## Description

The **favorite-things api** is the backbone of an application for keeping tracks of users favorite thing based on priority.

The API documentation can be found here: [![Run in Postman](https://run.pstmn.io/button.svg)]()

## Key Application features

1. Manage Favorite Things
2. Categorize Favorite Things
3. Set Priority on favorite things

## Set Up Development With Docker 

1. Download Docker from [here](https://docs.docker.com/)
2. Set up an account to download Docker
3. Install Docker after download
4. Go to your terminal run the command `docker login`
5. Input your Docker email and password

To setup for development with Docker after cloning the repository please do/run the following commands in the order stated below:

-   `cd <project dir>` to check into the dir
-   `docker-compose build` to build the application images
-   `docker-compose up -d` to start the api after the previous command is successful

The `docker-compose build` command builds the docker image where the api and its postgres database would be situated.
Also this command does the necessary setup that is needed for the API to connect to the database.

The `docker-compose up -d` command starts the application while ensuring that the postgres database is seeded before the api starts.

To stop the running containers run the command `docker-compose down`


**To Clean Up After using docker do the following**

1. run this command `docker ps` to view all docker images
2. run `docker stop ${image-id}`
2. run `docker rm ${image-id}`

**URGENT WARNING** PLEASE DO NOT RUN THE CLEAN-UP COMMAND ABOVE UNLESS YOU ARE ABSOLUTELY SURE YOU ARE DONE WITH THAT DEVELOPMENT SESSION AND HAVE NO DATA THAT WOULD BE LOST IF CLEAN-UP IS DONE!


### Alternative Development set up

-   Check that python 3 is installed:

    ```
    python --version
    >> Python 3.7
    ```

-   Install pipenv:

    ```
    brew install pipenv
    ```

-   Check pipenv is installed:
    ```
    pipenv --version
    >> pipenv, version 2018.6.25
    ```
-   Check that mysql is installed:

    ```
    mysql --version
    mysql  Ver 8.0.16 for osx10.14 on x86_64 (Homebrew)
    ```

-   Clone the favorite-things repo and cd into it:

    ```
    git clone https://github.com/koiic/favorite-things
    ```

-   Install dependencies:

    ```
    pipenv install
    ```


-   Make a copy of the .env.sample file  and rename it to .env and update the variables accordingly:

    ```
    FLASK_ENV = "development" # Takes either development, production, testing
    DATABASE_URI = "mysql+pymsql://YOUR_DB_USER:YOUR_DB_PASSWORD@YOUR_HOST/YOUR_DATABASE_NAME" # Development and production mySql db uri
    TEST_DATABASE_URI = "mysql+pymsql://YOUR_DB_USER:YOUR_DB_PASSWORD@YOUR_HOST/YOUR_TEST_DATABASE_NAME" # Testing mySql db uri
    JWT_SECRET_KEY_STAGING = "" # your prefered secret key
    API_BASE_URL_V1 = "" # The base url for V1 of the API
    ```

-   Activate a virtual environment:

    ```
    pipenv shell
    ```

-   Apply migrations:
    ```
    flask db init
    ```

    ```
    flask db upgrade
    ```
    
    ```
    flask db migrate
    ```



-   Run the application with either commands:

    ```
    python manage.py runserver 
    ```
    or
    ```
    flask run
    ```

-   Should you make changes to the database models, run migrations as follows

    -   Migrate database:

        ```
        flask db migrate
        ```

    -   Upgrade to new structure:
        ```
        flask db upgrade
        ```

-   Deactivate the virtual environment once you're done:
        ```
        exit
        ```  


- Entity Relation diagram
    ![Entity Diagram](entity.png)


