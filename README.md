# FlaskAPI
pip install mysql-connector-python


MySql Craete Table

CREATE TABLE Persons (
    Personid int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (Personid)
);


Curl Commands

Get Persons
----------------------
curl --location --request GET 'http://127.0.0.1:5000/MysqlPersons' \

Create Person
-----------------------

curl --location --request POST 'http://127.0.0.1:5000/MysqlPersons' \
--header 'Content-Type: application/json' \
--data-raw '{
    "Age":50,
    "LastName":"Rafi1",
    "FirstName":"sffdd"
}'

Update Person
---------------------
curl --location --request PUT 'http://127.0.0.1:5000/MysqlPersons' \
--header 'Content-Type: application/json' \
--data-raw '{
    "Age":53,
    "LastName":"Rafi Update",
    "FirstName":"sffdd",
    "Personid":6
}'

Delete Person
---------------------
curl --location --request DELETE 'http://127.0.0.1:5000/MysqlPersons' \
--header 'Content-Type: application/json' \
--data-raw '{
    "Personid":6
}'

Mongodb
--------
Get Persons
-----------------
curl --location --request GET 'http://127.0.0.1:5000/MongoDbPersons' \
--data-raw ''

Create Person
-----------------
curl --location --request POST 'http://127.0.0.1:5000/MongoDbPersons' \
--header 'Content-Type: application/json' \
--data-raw '{
    "Age":32,
    "LastName":"Rafi MongoDB Test",
    "FirstName":"sffdd"
}'

Update Person
--------------------
curl --location --request PUT 'http://127.0.0.1:5000/MongoDbPersons' \
--header 'Content-Type: application/json' \
--data-raw '{
    "Age":32,
    "LastName":"Rafi MongoDB Update Test",
    "FirstName":"sffdd",
    "Personid":"630101e9696ce651c28bce58"
}'

Delete Person
---------------------
curl --location --request DELETE 'http://127.0.0.1:5000/MongoDbPersons' \
--header 'Content-Type: application/json' \
--data-raw '{
    "Personid":"630101e9696ce651c28bce58"
}'


