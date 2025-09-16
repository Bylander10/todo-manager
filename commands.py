import argparse
from typing import List

from .models import Task
from .storage import load_tasks, save_tasks


def add_task(args: argparse.Namespace) -> None:
    tasks = load_tasks()
    new_task = Task(args.description)
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarefa adicionada: {new_task}")


def list_tasks(args: argparse.Namespace) -> None:
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def complete_task(args: argparse.Namespace) -> None:
    tasks = load_tasks()
    try:
        index = int(args.index) - 1
        if 0 <= index < len(tasks):
            tasks[index].mark_as_completed()
            save_tasks(tasks)
            print(f"Tarefa {args.index} marcada como concluída: {tasks[index]}")
        else:
            print(f"Índice inválido: {args.index}")
    except ValueError:
        print("Índice deve ser um número inteiro.")


def delete_task(args: argparse.Namespace) -> None:
    tasks = load_tasks()
    try:
        index = int(args.index) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            save_tasks(tasks)
            print(f"Tarefa deletada: {deleted}")
        else:
            print(f"Índice inválido: {args.index}")
    except ValueError:
        print("Índice deve ser um número inteiro.")
