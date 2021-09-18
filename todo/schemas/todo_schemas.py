from pydantic import BaseModel


def todoSerializer(todo) -> dict:
    return {
        "id" : str(todo["_id"]),
        "title": todo["title"],
        "text": todo["text"],
        "isCompleted": todo["isCompleted"]
    }
    



def todosSerializer(todos) -> list:
    return [todoSerializer(todo) for todo in todos]


