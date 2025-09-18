import argparse
import sys

from .commands import setup_parser, add_task, list_tasks, complete_task, delete_task


def main() -> None:
    parser = argparse.ArgumentParser(description='Gerenciador de Tarefas simples via linha de comando.')
    setup_parser(parser)

    args = parser.parse_args()
    if not hasattr(args, 'command') or args.command is None:
        parser.print_help()
        sys.exit(0)

    if args.command == 'add':
        add_task(args)
    elif args.command == 'list':
        list_tasks(args)
    elif args.command == 'complete':
        complete_task(args)
    elif args.command == 'delete':
        delete_task(args)
    else:
        parser.print_help()
        sys_exit(1)

if __name__ == '__main__':
    main()
