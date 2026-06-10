from models.base import BaseModel


class Task(BaseModel):
    def __init__(self, title):
        self.title = title
        self.completed = False

    # call this when the task is done
    def complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }
