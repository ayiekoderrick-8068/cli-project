from models.base import BaseModel



class Project(BaseModel):

    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

   
    def to_dict(self):
        return {
            "title": self.title,
            "tasks": [t.to_dict() for t in self.tasks]
        }
