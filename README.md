## Favorite things

This is an application built with flask(backend) and VueJs(frontend) the application allows users to create favorite things.

## Description

The **favorite-things application** keeps tracks of users favorite thing based on priority/ranking and it gives user access to view all favorite things that has been created by them.

## Key Application features

1. Manage Favorite Things
2. Categorize Favorite Things
3. Set Priority on favorite things

## Technology Used
 * Javascript(VueJS)
 * Python(Flask)
 * MySQL
 * Docker
 * SQLALCHEMY
 * MARSHMALLOW
    


## Set Up Development With Docker 

1. Download Docker from [here](https://docs.docker.com/)
2. Set up an account on Docker
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
    ##### BACKEND SET UP
     -   Clone the favorite-things repo and cd into it:
            git clone https://github.com/koiic/favorite-things
        
    -   CD into server folder 
    
    -   Create a .env file using the sample from .env.sample
    
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

 ##### FRONTEND SET UP
    -   CD into client folder 
    
    -   Check that Nodejs  and npm is installed:
    
        ```
        node --version
        >> v12.1.0
        npm --version
        >> 6.9.0
        ```
    
    -   Install dependencies:
    
        ```
        yarn install or npm install
        ```
    
    -   Run the application with either commands:
    
        ```
        yarn run serve
        ```
        or
        ```
        npm run serve
        ```
 
 ##### TEST RUNNER
    -   CD into server folder 
    
    -   run test with the command below:
    
        ```
        pytest
        ```
    
 
### Deployment Setup
Follow this steps to deploy the application on AWS(EC2 instance)
 1. If you already have an AWS Account, Launch a new EC2 instance
 2. If not register on AWS and create an account 
    * configure port and other settings
 3. generate your keypair in order to use it to SSH into your instance
 4. Depending on the server you choose if for example you choose UBUNTU server
 5. SSH into your server: ``` ssh -i /path_to_key/my_key.pem user_name@public_dns_name```
 6. Install Docker : ```sudo apt-get update``` ```sudo apt-get install docker-ce```
 7. clone the repository to your new hosting environment  : ``` git clone https://github.com/koiic/favorite-things.git ```
 8. create a .env file copy the content from the .env.sample file and paste it on the root folder, edit the config to fit your setup ```nano .env```
 9. run ``` cp .env server/.env```
 10. Change directory into app/client create a .env ``` touch .env``` copy the file in ```app/client/.env.sample``` to ```.env```
 11. Run the following command ``` chmod 444 deployment.sh``` to give permission to the bash script
 12. Run ``` bash deployment.sh``` this command will build the docker instance and the application will be served through this URL:
     * SERVER API's:/5000
     * FRONTEND URL: /8000
 
 
  ### Step taken to autolint code

    For the server side I made use of PYLINT:
        this is a linting tool for python that help me follow the python style guide

    
    for the frontend 
        I used ESLINT folling the airbnb configuration style guide
        

- Entity Relation diagram
    ![Entity Diagram](entity.png)


