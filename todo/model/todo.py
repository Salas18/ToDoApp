class Todo:
    mark_completed: True
    def __init__(self, code_id : int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self, completed : bool = True):
        return completed

    def add_tagg(self, tag: str):
        for tag in self.tags:
            if tag is not self.tags:
                self.tags.append(tag)

    def __str__(self,):
        return f'{self.code_id}-{self.title}'

class TodoBook:
    def __init__(self, todos):
        self.todos: dict = {}

    def inicializador:
        pass




















