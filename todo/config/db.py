from pymongo import MongoClient

client = MongoClient("mongodb+srv://eslam:eslam@todocluster.tdbat.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.todo_application
collection_name = db['todo_app']

