from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    item: str

    model_config = {
        "json_schema_extra" : {
            "examples": [
                {
                "id": 1,
                "item": "Example schema!"
            }
            ]
        }
    }

class TodoItem(BaseModel):
    item: str

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "item": "Read the next chapter of the book"
            }]
        }
    }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    model_config = {
        "json_schema_extra": {
            "example": {
                "todos": [
                    {
                "item": "Example schema! 1"
            },
            {
                "item": "Example schema! 2"
            }
                ]
            }
        }
    }