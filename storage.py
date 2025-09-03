import json
from typing import List
from datetime import datetime

from .models import Task


def task_to_dict(task: Task) -> dict:
    return {
        "description": task.description,
        "completed": task.completed,
        "created_at": task.created_at.isoformat()
    }


def dict_to_task(data: dict) -> Task:
    task = Task(data["description"])
    task.completed = data.get("completed", False)
    task.created_at = datetime.fromisoformat(data["created_at"])
    return task


def load_tasks(file_path: str = "todos.json") -> List[Task]:
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return [dict_to_task(item) for item in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise ValueError("Arquivo JSON corrompido.")


def save_tasks(tasks: List[Task], file_path: str = "todos.json") -> None:
    data = [task_to_dict(task) for task in tasks]
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
