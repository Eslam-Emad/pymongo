from fastapi import FastAPI
from todo.routers import todo_route  

        
app = FastAPI()


app.include_router(todo_route.router)