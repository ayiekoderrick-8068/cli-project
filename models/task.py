from models.base import BaseModel


# A task belongs to a project, it starts as not completed
class Task(BaseModel):

    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True

    # converts the task to a dictionary for saving
    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }
