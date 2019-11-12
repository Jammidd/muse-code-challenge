Muse Job Search
===============

Job Search tool for The Muse coding challenge

<a href="https://github.com/vchaptsev/cookiecutter-django-vue">
    <img src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Vue-blue.svg" />
</a>


## Getting Started

1. Install [Docker](https://docs.docker.com/install/) and [Docker-Compose](https://docs.docker.com/compose/). Start your virtual machines with the following shell command:

`docker-compose up --build`

2. Connect to the docker API container

`docker exec -it muse_code_challenge_backend_1 /bin/bash`

3. Populate the job table with data from The Muse API. If no job count is provided, 40 jobs will be added.

`python manage.py populate_jobs -n <number-of-jobs-to-add>` 

4. Access and test the UI

`http://localhost:8000`

5. API URL

`http://localhost:8000/api`
