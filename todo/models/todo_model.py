from pydantic import BaseModel

class Todo(BaseModel):
    title:str
    text:str
    isCompleted:bool
    date:str
