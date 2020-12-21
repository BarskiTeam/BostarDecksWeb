# BostarDecksWeb

### For develepor - start working with repo

1 _Clonning repository_

`git clone https://github.com/BarskiTeam/BostarDecksWeb.git`

2 _Inside we are creating virtual environment_

`virtualenv venv`

3 _Sourcing virtual environment_

`source venv/bin/activate`

4 _Installing pipenv_ 

We are installing pipenv library this is help to show
dependency between python libraries.

`pip install --upgrade pip`

`pip install pipenv`

5 _Installing library from Pipfile _

`pipenv source`

6 _.env and database postgres_

In main folder of project we find file with name .env.example. Inside them, we will find
environmental variable essential for database (number of port, name of database etc)

ATTENTION - adding new variable to .env, you need add this to .env.example, too.

`cp .env.example .env`

ofcourse you can change default value (and even you should !)

7 _Starting with database container_

Uruchomienie dockera ( z)
Running database container with docker ( I assume you have installated docker )

`docker-compose up`

If you need stop container, i recomended ctrl + c or

`docker-compose stop`

to remove 

`docker-compose down`

if you will see problem with number of port, check ports of running container

`docker ps` 

8 _Migration database_

Ok, now we are doing migration of core/models.py of bostardeckweb project

`python manage.py migrate`
`python manage.py makemigrations`

9 _We need create of superuser_

`python manage.py createsuperuser`

and after we will need write his nick, email and password

10 _Running web_

`python manage.py runserver` #default port 8000

11 _Administrator panel_

To use administrator panel you use this url
`127.0.0.1:8000/admin`

and voila we are ready to work !