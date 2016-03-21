# wordchain
A word chain game run on the web. See https://en.wikipedia.org/wiki/Word_chain

# prerequisite
### This instruction is written for user who use ubuntu environment (or cloud9 ide)
1. django should be installed on python version 3.x
  * sudo pip3 install django

2. django-decorator-include package should be installed
  * sudo pip3 install django-decorator-include

3. konlpy package should be installed. To do this, jdk also should be installed
  * sudo apt-get install openjdk-7-jdk
  * sudo pip3 install konlpy

4. try starting server (on_your_workspace/src)
  * python3 manage.py runserver 0.0.0.0:8080
