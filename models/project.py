class Project:
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            "title": self.title,
            "tasks": [task.to_dict() for task in self.tasks]
        }
