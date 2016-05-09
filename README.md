# wordchain
A word chain game run on the web. See https://en.wikipedia.org/wiki/Word_chain

##### This instruction is written for user who use ubuntu environment (or cloud9 ide)

# Prerequisite
#### Install framework and modules for project
##### 1. django should be installed on python version 3.x
  * sudo pip3 install django

##### 2. django-decorator-include package should be installed
  * sudo pip3 install django-decorator-include

##### 3. konlpy package should be installed. To do this, jdk also should be installed
  * sudo apt-get install openjdk-7-jdk
  * sudo pip3 install konlpy

#### Make migrations for game app (from models of game) and migrate it into detabase
##### 1. make migrations of game app
  * python3 manage.py makemigrations game

##### 2. migrate migrations into database
  * python3 manage.py migrate

#### Create super user for admin (and for first player)
##### 1. use manager option 'createsuperuser'
  * python3 manage.py createsuperuser

##### 2. follow instruction to create admin user

#### Run server for project
##### 1. try starting server (on_your_workspace/src)
  * python3 manage.py runserver 0.0.0.0:8080

#### Install PhantomJS for web testing
##### 1. sudo pip3 install selenium
##### 2. sudo npm -g install phnatomjs
