from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models import TaskDB
from schemas import Task

router = APIRouter()

@router.post("/tasks")
def create_task(task: Task):
    db = SessionLocal()

    new_task = TaskDB(
    title=task.title,
    description=task.description,
    completed=task.completed,
    priority=task.priority,
    due_date=task.due_date
)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    db.close()

    return {"message": "Task created", "task_id": new_task.id}


@router.get("/tasks")
def get_tasks():
    db = SessionLocal()
    tasks = db.query(TaskDB).all()
    db.close()
    return tasks


@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    db = SessionLocal()

    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()

    if not task:
        db.close()
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = updated_task.title
    task.description = updated_task.description
    task.completed = updated_task.completed
    task.priority = updated_task.priority
    task.due_date = updated_task.due_date

    db.commit()
    db.close()

    return {"message": "Task updated"}


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db = SessionLocal()

    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()

    if not task:
        db.close()
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    db.close()

    return {"message": "Task deleted"}

@router.get("/tasks/search")
def search_tasks(keyword: str):
    db = SessionLocal()
    tasks = db.query(TaskDB).filter(
        TaskDB.title.contains(keyword)
    ).all()
    db.close()
    return tasks

@router.get("/tasks/completed")
def completed_tasks():
    db = SessionLocal()
    tasks = db.query(TaskDB).filter(
        TaskDB.completed == True
    ).all()
    db.close()
    return tasks

@router.get("/tasks/pending")
def pending_tasks():
    db = SessionLocal()
    tasks = db.query(TaskDB).filter(
        TaskDB.completed == False
    ).all()
    db.close()
    return tasks