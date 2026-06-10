from models.base import BaseModel


class User(BaseModel):
    def __init__(self, name):
        self.name = name
        self.projects = []  # starts with no projects

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "name": self.name,
            "projects": [p.to_dict() for p in self.projects]
        }
