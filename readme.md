# SportsRoom

readme-v1
## Sec - 1: Preamble

- This is part of a course project, under the course SoftwareProductionEngineering.
- This is a web app, which can be used to manage and distribute the sports equiment and sports grounds of an organisation.
- Built using django-python, celery (for job scheduling, for updating penalty, and some other stuff)
- The aim of this project is to introduce us to industry's Software Development & Operations' Toolchains, Pipelines, etc.
- Collaborators Kartik Gupta, Lalith Kota, Swastik Shrivastava.

## Sec - 2: Small-Note Before Running

- Make sure you have a config file with the SMTP mail and Password setup, inside your `$HOME/myConfigs/sportsRoom.conf`, of this Format:
  ```
  {
    'smtp':{
      'username':<>,
      'password':<>
    }
  }
  ```
- Also make sure your DB, the celery beat DB are present in the `$HOME/myDb/sportsRoom-Db.sqlite3` and `$HOME/myDb/sportsRoom-celerybeat-schedule`.
- These directories, `myDb` and `myConfigs`, will be mounted inside the docker container, at `/myDb` & `/myConfigs`.

## Sec - 3: How to Run

- To run locally:
  - first install the requirements, from the requirements.txt. Using:
    - `python3 install -r requirements.txt`
  - Then makemigrations migrate and runserver:
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
    - `python3 manage.py runserver`
  - Also, to use the celery scheduler make sure the redis-server & celery are already installed. Then use these cmds to start them.
  If you dont want to run/test this scheduling parts (net equipment quantity mails, penalty mails, invalid user removal, etc)
  then you can skip this part.
    - `redis-server`
    - `celery -A sportsroom worker -l info`
    - `celery -A sportsroom beat -l info -s ~/myDb/sportsRoom-celerybeat-schedule`
- Instead you can simply use this [docker image](https://hub.docker.com/r/lalithkota/sportsroom)
