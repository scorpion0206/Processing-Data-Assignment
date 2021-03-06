# Processing Data - Trial Assignment B

This represents a project given as a job application assignment by Adivare BV.

### Prerequisites for running the application

##### Packages
- Run **pip install -r requirements.txt** to install all the necessary packages

##### Docker containers with respective commands:

1. **redis queue #1:** 

    docker run -d -p 6379:6379 --name redis-redisjson redislabs/rejson:latest

2. **redis queue #2:**

    docker run -d -p 6380:6379 --name redis-redisjson2 redislabs/rejson:latest

3. **redis queue #3:**

    docker run -d -p 6381:6379 --name redis-redisjson3 redislabs/rejson:latest

3. **PostgreSQL database:** 

    docker run -p 5432:5432 -e POSTGRES_DB=postgres_database -e POSTGRES_USER=postgres_user -e POSTGRES_PASSWORD=postgres_password -d postgres

##### Python scripts that need to be started:

1. **inject_data.py**
    - creates fake data
    - injects the data on the pre-processing queue
    - user inputs 1 for complete data and 0 for incomplete data (which is used later
     for testing the de-duplication process)
    - offers logs about the data creation process
    - the data can be found on the Redis Queue #1

2. **check_data.py**
    - reads data from the previous queue
    - validates and grades the data
    - if necessary, de-duplicates data
    - grades and pre-processed data (takes care of duplcated items as well)
    - stores the data in the second Redis Queue
    
##### Django management commands (run as **python manage.py -command- **)

1. **makemigrations**

2. **migrate**

3.  **store_data**
    - reads data from Redis Queue #2
    - creates the models (while validating the data once again at the same time)
    - stores them in the PostgreSQL Database

4. **createsuperuser**
    - required in order to get admin privileges

##### Web Interface

1. **http://localhost:8000/admin/**
    - The Database Models are present here
    - Upon clicking on one of them, the user is greeted with the list of database entries of that model
    - The entry can be modified or deleted

2. **http://localhost:8000/grading_queue/**
    - Displays the items currently in the Grading Queue as HTML tables

3. **http://localhost:8000/dedup_queue/**
    - Displays the items currently in the De-duplication Queue as HTML tables

4. **http://localhost:8000/poison_queue/**
    - Displays the items currently in the Poison Queue as HTML tables

##### Miscellaneous Django management commands with their respective effects:

* manage.py runserver: starts the Django server on the default port, localhost:8000/

* manage.py read_json "file_name" : reads the json file and outputs the formatted data 

* manage.py read_xml "file_name" : reads the xml file and outputs the formatted data 


##### PostgreSQL admin user details:
* user: postgres_user
* password: postgres_password
* host: localhost
* port: 5432
* name: postgres_database
