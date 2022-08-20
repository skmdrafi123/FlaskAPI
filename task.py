from bson import BSON
from flask import Flask, request, jsonify
import mysql.connector
import pymongo
from bson.json_util import dumps, loads
from bson.objectid import ObjectId

mydb = mysql.connector.connect(
  host="localhost",
  user="rafi",
  password="12345678",
  database="rafi"
)

client = pymongo.MongoClient("mongodb+srv://skmdrafi:Eg3d4QFPLjZBEeEa@cluster0.1vcbf.mongodb.net/?retryWrites=true&w=majority")

app = Flask(__name__)

@app.route('/MysqlPersons/', methods=['GET', 'POST','PUT','DELETE'])
def Sqlpersons():
    if (request.method == 'GET'):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM persons")
        myresult = mycursor.fetchall()
        return jsonify(myresult)

    if (request.method == 'POST'):
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        Age = request.json['Age']
        mycursor = mydb.cursor()
        sql = "INSERT INTO persons (LastName, FirstName,Age) VALUES (%s, %s, %s)"
        val = (LastName, FirstName,Age)
        mycursor.execute(sql, val)
        mydb.commit()
        id = mycursor.lastrowid
        return jsonify((str('Inserted Successfully:'+str(id))))

    if (request.method == 'PUT'):
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        Age = request.json['Age']
        id = request.json['Personid']

        mycursor = mydb.cursor()
        sql = "update persons set LastName =%s,FirstName =%s,Age =%s where Personid = '%s'"
        val = (LastName, FirstName, Age,id)
        mycursor.execute(sql,val)
        mydb.commit()
        return 'Updated Successfully'

    if (request.method == 'DELETE'):
        id = request.json['Personid']

        mycursor = mydb.cursor()
        sql = "DELETE FROM  persons where Personid = '%s'"%(id)
        mycursor.execute(sql)
        mydb.commit()
        return 'Deleted Successfully'

@app.route('/MongoDbPersons/', methods=['GET', 'POST','PUT','DELETE'])
def MongoPersons():
    if (request.method == 'GET'):
        db1 = client['mongotest']
        coll = db1['Persons']
        x = coll.find({})
        json_data = dumps(list(x), indent=2)
        return json_data

    if (request.method == 'POST'):
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        Age = request.json['Age']
        d = {
            "LastName": LastName,
            "FirstName": FirstName,
            "Age": Age
        }
        db1 = client['mongotest']
        coll = db1['Persons']
        x = coll.insert_one(d)
        d1= x.inserted_id
        return jsonify((str('Inserted Successfully:'+str(d1))))

    if (request.method == 'PUT'):
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        Age = request.json['Age']
        id = request.json['Personid']

        db1 = client['mongotest']
        coll = db1['Persons']
        x = coll.find_one()
        d = {
            "LastName": LastName,
            "FirstName": FirstName,
            "Age": Age
        }
        coll.update_many({'_id': ObjectId(id)}, {"$set":d})
        return 'Updated Successfully'

    if (request.method == 'DELETE'):
        id = request.json['Personid']

        db1 = client['mongotest']
        coll = db1['Persons']

        x = coll.delete_one({'_id': ObjectId(id)})
        return 'Deleted Successfully'

if __name__ == '__main__':
    app.run()