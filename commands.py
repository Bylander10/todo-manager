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


def setup_parser(parser: argparse.ArgumentParser) -> None:
    

    # Cria o grupo de comandos apenas UMA vez
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponíveis')

    # subcomando para criar tarefa
    add_parser = subparsers.add_parser('add', help='Adiciona uma tarefa')
    add_parser.add_argument('description', type=str, help='Descrição da Tarefa')

    # subcomando pra listar
    subparsers.add_parser('list', help='Lista tarefas')

    # subcomando pra completar tarefa
    complete_parser = subparsers.add_parser('complete', help='Marca tarefa como concluída')
    complete_parser.add_argument('index', type=str, help='Índice da tarefa (inicia em 1)')

    # subcomando pra deletar tarefa
    delete_parser = subparsers.add_parser('delete', help='Deleta uma tarefa')
    delete_parser.add_argument('index', type=str, help='Índice da tarefa (inicia em 1)')
