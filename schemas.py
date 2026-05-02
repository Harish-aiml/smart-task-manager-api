from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    title: str
    description: str
    completed: bool = False
    priority: str = "medium"
    due_date: Optional[str] = None