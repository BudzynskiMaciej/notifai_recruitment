# Textify App

This is rest api that allow store, edit and delete custom text notes. It is written in [Python] v3.7 and [Django] v3.2.3. 
It uses [PostgreSQL] as database engine on production and [SQLite] for testing. Application is deployed on [Heroku]. 

## Table of content

- [Table of content](#table-of-content)
- [REST Endpoints](#rest-endpoints)
  * [Get list of all available routes for API](#get-list-of-all-available-routes-for-api)
    + [Request](#request)
    + [Response](#response)
  * [Get list of all notes](#get-list-of-all-notes)
    + [Request](#request-1)
    + [Response](#response-1)
  * [Create a new note](#create-a-new-note)
    + [Request](#request-2)
    + [Response](#response-2)
  * [Get a specific note](#get-a-specific-note)
    + [Request](#request-3)
    + [Response](#response-3)
  * [Edit a note](#edit-a-note)
    + [Request](#request-4)
    + [Response](#response-4)
  * [Delete a note](#delete-a-note)
    + [Request](#request-5)
    + [Response](#response-5)
- [Download](#download)
- [Running project](#running-project)
- [Testing project](#testing-project)
- [Deploy on Heroku](#deploy-on-heroku)
- [Sphinx Documentation](#sphinx-documentation)
- [Contact](#contact)
- [License](#license)

## REST Endpoints

Application is running on production on [https://notifai-textify.herokuapp.com/api/v1/](https://notifai-textify.herokuapp.com/api/v1/)

The REST API to the Textify App is described below with example requests via [curl].

### Get list of all available routes for API

#### Request

`GET /api/v1/`

    curl -X GET https://notifai-textify.herokuapp.com/api/v1/

#### Response

    HTTP/1.1 200 OK
    Connection: keep-alive
    Server: gunicorn
    Date: Fri, 21 May 2021 10:33:06 GMT
    Content-Type: application/json
    Allow: GET, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 63
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Via: 1.1 vegur

    {"notes":"https://notifai-textify.herokuapp.com/api/v1/notes/"}

### Get list of all notes

#### Request

`GET /api/v1/notes`

    curl -X GET https://notifai-textify.herokuapp.com/api/v1/notes/

#### Response

    HTTP/1.1 200 OK
    Connection: keep-alive
    Server: gunicorn
    Date: Fri, 21 May 2021 10:39:39 GMT
    Content-Type: application/json
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 2
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Via: 1.1 vegur

    []

### Create a new note

#### Request

`POST /api/v1/notes`

Authentication with `HEADER 'Bearer: P@s$w0rd'`

    curl -X POST https://notifai-textify.herokuapp.com/api/v1/notes/ -H 'Bearer: P@s$w0rd' -d message="Hello there"

#### Response

    HTTP/1.1 201 Created
    Connection: keep-alive
    Server: gunicorn
    Date: Fri, 21 May 2021 10:41:57 GMT
    Content-Type: application/json
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 47
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Via: 1.1 vegur

    {"id":1,"message":"Hello there","view_count":0}

### Get a specific note

#### Request

`GET /api/v1/notes/:id/`

    curl -X GET https://notifai-textify.herokuapp.com/api/v1/notes/1/

#### Response

    Connection: keep-alive
    Server: gunicorn
    Date: Fri, 21 May 2021 10:48:03 GMT
    Content-Type: application/json
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 47
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Via: 1.1 vegur

    {"id":1,"message":"Hello there","view_count":1}

### Edit a note

#### Request

`PUT /api/v1/notes/:id/`

`HEADER 'Bearer: P@s$w0rd'`
   
        curl -X PUT https://notifai-textify.herokuapp.com/api/v1/notes/1/ -H 'Bearer: P@s$w0rd' -d message="Hello World!"

#### Response

    HTTP/1.1 200 OK
    Connection: keep-alive
    Server: gunicorn
    Date: Fri, 21 May 2021 10:52:35 GMT
    Content-Type: application/json
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 48
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Via: 1.1 vegur

    {"id":1,"message":"Hello World!","view_count":0}

### Delete a note

#### Request

`DELETE /api/v1/notes/:id/`

`HEADER 'Bearer: P@s$w0rd'`

    curl -X DELETE https://notifai-textify.herokuapp.com/api/v1/notes/2/ -H 'Bearer: P@s$w0rd'

#### Response

    HTTP/1.1 204 No Content
    Connection: keep-alive
    Server: gunicorn
    Date: Fri, 21 May 2021 10:59:10 GMT
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 0
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Via: 1.1 vegur

`` ``

## Download

You can use one of the following methods for download:
 - Run the command below with the command line utility with GIT installed:
  ```sh
  git clone https://github.com/BudzynskiMaciej/notifai_recruitment.git
  cd Django-Project/
  git checkout develop
  ```
  - [Download zip file](https://github.com/BudzynskiMaciej/notifai_recruitment/archive/develop.zip)
 
## Running project

Before opening project u need to create .env file. There are [.env.example](.env.example), so use its content to implement 
needed enviroment variables. MASTER_KEY is used for authorization in headers. The rest can be left unchanged.
To run the project you need the [docker] and [docker-compose] tools.
After [download](#download) in project directory run the command:
```sh
docker-compose up -d
```
After running the project, you need to migrate the database and create a superuser. To do this, run the following 
commands while the containers are running:
```sh
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py initadminacc
```

You can test this solution on your computer. See [REST Endpoints](#rest-endpoints) for testing. Remember that the base 
url now is not [https://notifai-textify.herokuapp.com/](https://notifai-textify.herokuapp.com/), but it is 
[http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Testing project

Testing uses [SQLite] database so can be used in local enviroment or when docker container is running.
To run test with docker, make sure the container is running and then:
```sh
docker-compose exec web python manage.py test
```

To run test on local machine u to have installed and activated [virtualenv].
Then install the project [requirements.txt](requirements.txt). To do this, run the following command in the project directory:
```sh
pip install -r requirements.txt
```

To test the project locally, you can use the following commands:
```sh
python manage.py test
coverage run --source='.' manage.py test
coverage html
```

## Deploy on Heroku

Deploying on heroku is simple. In order to release the applications You must follow these steps:

1. Create a new github repo and set a Secret on Repo Settings Page `HEROKU_API_KEY`
2. To get a `HEROKU_API_KEY` you need to login to your heroku account and go to API Key in Account Settings. Copy it to 
   your repo settings on github.
3. On Heroku page create a new project and go it's settings and then Config Vars. You need to create all enviroment 
   variables that are listed in [.env.example](.env.example). Remember to change user creditentials and MASTER_KEY.
4. Edit [.github/workflows/main.yml](.github/workflows/main.yml) setting ur heroku email, app name (unique for heroku) 
   and branch that app is deployed from.
5. Commit changes and push to remote repository on github.
6. On Heroku project page select Deploy tab and Deployment method as Github.
7. Choose repository you want to deploy and branch specified in step 4. Enable Automatic Deploys.
8. If somethink goes wrong use Manual Deploy.

Application should deploy each time it will detect changes on specific branch. For my project it is develop branch.

## Sphinx Documentation

[https://budzynskimaciej.pl/notifai_recruitment/](https://budzynskimaciej.pl/notifai_recruitment/)

## Contact

[kontakt@budzynskimaciej.pl](mailto:kontakt@budzynskimaciej.pl)

## License

[MIT](LICENSE)

[Python]: <https://www.python.org/>
[Django]: <https://www.djangoproject.com/>
[PostgreSQL]: <https://www.postgresql.org/>
[SQLite]: <https://www.sqlite.org/>
[Heroku]: <https://heroku.com/>
[curl]: <https://curl.se/>
[docker]: <https://www.docker.com/>
[docker-compose]: <https://docs.docker.com/compose/>
[virtualenv]: <https://virtualenv.pypa.io/en/stable/>
