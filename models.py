from datetime import datetime


class Task:

    def __init__(self, description: str) -> None:
        self.description = description
        self.completed = False
        self.created_at = datetime.now()

    def mark_as_completed(self) -> None:
        self.completed = True

    def __str__(self) -> str:
        status = "[Concluída]" if self.completed else "[Pendente]"
        return f"{self.description} {status} - Criada em: {self.created_at.strftime('%d-%m-%Y %H:%M')}"

