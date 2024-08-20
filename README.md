Planetarium API Project

API service for planetarium management written on DRF

Test account: username: test@user.com , password: testpassword

Installation
Install PostgresSQL and create db

git clone https://github.com/KravchenkoSerhiii/planetarium-api.git
cd planetarium_api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
set DB_HOST=<your db host name>
set DB_NAME=<your db name>
set DB_USER=<your db username>
set DB_PASSWORD=<your db password>
set SECRET_KEY=<your secret key>
python manage.py migrate
python manage.py runserver

Run with docker

Docker should be installed
docker-compose build
docker-compose up

Getting access
create user via api/vi/user/register/
get access token via api/v1/user/token/


Features
JWT authenticated
Admin panel /admin/
Documentation is located at api/doc/swagger/
Managing orders and tickets
Creating planetariums, show themes, show sessions, astronomy shows
