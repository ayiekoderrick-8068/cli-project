class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }
