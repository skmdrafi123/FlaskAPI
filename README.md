# FlaskAPI

Curl Commands

Get Persons
----------------------
curl --location --request GET 'http://127.0.0.1:5000/MysqlPersons' \
--header 'Content-Type: application/json' \
--data-raw '{
    "Age":10,
    "LastName":"Rafi1",
    "FirstName":"sffdd",
    "Personid":51
}'

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


