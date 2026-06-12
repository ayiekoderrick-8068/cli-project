from models.base import BaseModel


# A project belongs to a user and holds a list of tasks
class Project(BaseModel):

    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    # converts the project to a dictionary for saving
    def to_dict(self):
        return {
            "title": self.title,
            "tasks": [t.to_dict() for t in self.tasks]
        }
