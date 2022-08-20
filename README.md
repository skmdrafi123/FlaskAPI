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
