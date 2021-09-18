from todo.models.todo_model import Todo
from fastapi import APIRouter
from ..repository import todo_repo as repo 


router = APIRouter()

@router.get("/")
async def retriveAll():
    return  repo.retriveAll()

@router.get("/{id}")
async def retrive_one(id:str):
    return  repo.retrive_one(id)

@router.post("/")
async def post(todo :Todo):
    return repo.post(todo)


@router.put("/{id}")
async def put(id:str , todo:Todo):
    return repo.put(id , todo)


@router.delete("/{id}")
async def delete(id:str):
    return repo.delete(id)