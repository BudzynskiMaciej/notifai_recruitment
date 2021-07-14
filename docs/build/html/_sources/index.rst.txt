.. Textify documentation master file, created by
   sphinx-quickstart on Mon May 17 21:17:58 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Textify's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Textify App
===========

This is rest api that allow store, edit and delete custom text notes. It
is written in `Python <https://www.python.org/>`__ v3.7 and
`Django <https://www.djangoproject.com/>`__ v3.2.3. It uses
`PostgreSQL <https://www.postgresql.org/>`__ as database engine on
production and `SQLite <https://www.sqlite.org/>`__ for testing.
Application is deployed on `Heroku <https://heroku.com/>`__.

Table of content
----------------

-  `Table of content <#table-of-content>`__
-  `REST Endpoints <#rest-endpoints>`__
-  `Get list of all available routes for
   API <#get-list-of-all-available-routes-for-api>`__

   -  `Request <#request>`__
   -  `Response <#response>`__

-  `Get list of all notes <#get-list-of-all-notes>`__

   -  `Request <#request-1>`__
   -  `Response <#response-1>`__

-  `Create a new note <#create-a-new-note>`__

   -  `Request <#request-2>`__
   -  `Response <#response-2>`__

-  `Get a specific note <#get-a-specific-note>`__

   -  `Request <#request-3>`__
   -  `Response <#response-3>`__

-  `Edit a note <#edit-a-note>`__

   -  `Request <#request-4>`__
   -  `Response <#response-4>`__

-  `Delete a note <#delete-a-note>`__

   -  `Request <#request-5>`__
   -  `Response <#response-5>`__

-  `Download <#download>`__
-  `Running project <#running-project>`__
-  `Testing project <#testing-project>`__
-  `Deploy on Heroku <#deploy-on-heroku>`__
-  `Contact <#contact>`__
-  `License <#license>`__

REST Endpoints
--------------

Application is running on production on
https://notifai-textify.herokuapp.com/api/v1/

The REST API to the Textify App is described below with example requests
via `curl <https://curl.se/>`__.

Get list of all available routes for API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request
^^^^^^^

``GET /api/v1/``

::

    curl -X GET https://notifai-textify.herokuapp.com/api/v1/

Response
^^^^^^^^

::

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

Get list of all notes
~~~~~~~~~~~~~~~~~~~~~

Request
^^^^^^^

``GET /api/v1/notes``

::

    curl -X GET https://notifai-textify.herokuapp.com/api/v1/notes/

Response
^^^^^^^^

::

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

Create a new note
~~~~~~~~~~~~~~~~~

Request
^^^^^^^

``POST /api/v1/notes``

Authentication with ``HEADER 'Bearer: P@s$w0rd'``

::

    curl -X POST https://notifai-textify.herokuapp.com/api/v1/notes/ -H 'Bearer: P@s$w0rd' -d message="Hello there"

Response
^^^^^^^^

::

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

Get a specific note
~~~~~~~~~~~~~~~~~~~

Request
^^^^^^^

``GET /api/v1/notes/:id/``

::

    curl -X GET https://notifai-textify.herokuapp.com/api/v1/notes/1/

Response
^^^^^^^^

::

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

Edit a note
~~~~~~~~~~~

Request
^^^^^^^

``PUT /api/v1/notes/:id/``

``HEADER 'Bearer: P@s$w0rd'``

::

        curl -X PUT https://notifai-textify.herokuapp.com/api/v1/notes/1/ -H 'Bearer: P@s$w0rd' -d message="Hello World!"

Response
^^^^^^^^

::

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

Delete a note
~~~~~~~~~~~~~

Request
^^^^^^^

``DELETE /api/v1/notes/:id/``

``HEADER 'Bearer: P@s$w0rd'``

::

    curl -X DELETE https://notifai-textify.herokuapp.com/api/v1/notes/2/ -H 'Bearer: P@s$w0rd'

Response
^^^^^^^^

::

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

\`\` \`\`

Download
--------

You can use one of the following methods for download: - Run the command
below with the command line utility with GIT installed:
``sh   git clone https://github.com/BudzynskiMaciej/notifai_recruitment.git   cd Django-Project/   git checkout develop``
- `Download zip
file <https://github.com/BudzynskiMaciej/notifai_recruitment/archive/develop.zip>`__

Running project
---------------

Before opening project u need to create .env file. There are
`.env.example <.env.example>`__, so use its content to implement needed
enviroment variables. MASTER\_KEY is used for authorization in headers.
The rest can be left unchanged. To run the project you need the
`docker <https://www.docker.com/>`__ and
`docker-compose <https://docs.docker.com/compose/>`__ tools. After
`download <#download>`__ in project directory run the command:

.. code:: sh

    docker-compose up -d

After running the project, you need to migrate the database and create a
superuser. To do this, run the following commands while the containers
are running:

.. code:: sh

    docker-compose exec web python manage.py migrate --noinput
    docker-compose exec web python manage.py initadminacc

You can test this solution on your computer. See `REST
Endpoints <#rest-endpoints>`__ for testing. Remember that the base url
now is not https://notifai-textify.herokuapp.com/, but it is
http://127.0.0.1:8000/.

Testing project
---------------

Testing uses `SQLite <https://www.sqlite.org/>`__ database so can be
used in local enviroment or when docker container is running. To run
test with docker, make sure the container is running and then:

.. code:: sh

    docker-compose exec web python manage.py test

To run test on local machine u to have installed and activated
`virtualenv <https://virtualenv.pypa.io/en/stable/>`__. Then install the
project `requirements.txt <requirements.txt>`__. To do this, run the
following command in the project directory:

.. code:: sh

    pip install -r requirements.txt

To test the project locally, you can use the following commands:

.. code:: sh

    python manage.py test
    coverage run --source='.' manage.py test
    coverage html

Deploy on Heroku
----------------

Deploying on heroku is simple. In order to release the applications You
must follow these steps:

1. Create a new github repo and set a Secret on Repo Settings Page
   ``HEROKU_API_KEY``
2. To get a ``HEROKU_API_KEY`` you need to login to your heroku account
   and go to API Key in Account Settings. Copy it to your repo settings
   on github.
3. On Heroku page create a new project and go it's settings and then
   Config Vars. You need to create all enviroment variables that are
   listed in `.env.example <.env.example>`__. Remember to change user
   creditentials and MASTER\_KEY.
4. Edit `.github/workflows/main.yml <.github/workflows/main.yml>`__
   setting ur heroku email, app name (unique for heroku) and branch that
   app is deployed from.
5. Commit changes and push to remote repository on github.
6. On Heroku project page select Deploy tab and Deployment method as
   Github.
7. Choose repository you want to deploy and branch specified in step 4.
   Enable Automatic Deploys.
8. If somethink goes wrong use Manual Deploy.

Application should deploy each time it will detect changes on specific
branch. For my project it is develop branch.

Contact
-------

kontakt@budzynskimaciej.pl

License
-------

`MIT <LICENSE>`__
