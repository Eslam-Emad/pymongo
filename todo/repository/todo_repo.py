from bson.objectid import ObjectId
from fastapi.exceptions import HTTPException
from starlette import status
from ..config.db import collection_name
from ..models.todo_model import Todo
from ..schemas.todo_schemas import *

def retriveAll():
    todos =  collection_name.find()
    if not todos :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=  f'there is no Todos')
    return {"status" : "ok" , "data" : todosSerializer(todos)}

   

def retrive_one(id:str):
    todo =  collection_name.find_one({"_id" : ObjectId(id)})
    if not todo :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=  f'there is no Todos')
    return {"status" : "ok" , "data" : todoSerializer(todo)}



def post(todo :Todo):
    insertedTodo = collection_name.insert_one(dict(todo))
    todoItem = collection_name.find({"_id" : insertedTodo.inserted_id})
    return todosSerializer(todoItem)
    

def put(id: str , todo:Todo):
    item = collection_name.find_one_and_update({"_id" : ObjectId(id)} , {
        "$set": dict(todo)
    })
    return todoSerializer(collection_name.find_one({"_id": ObjectId(id)}))



def delete(id:str):
    collection_name.find_one_and_delete({"_id" : ObjectId(id)})
    return {"status" : "Done!"}
