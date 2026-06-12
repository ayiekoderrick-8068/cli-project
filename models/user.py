from models.base import BaseModel


# A user has a name and a list of projects they own
class User(BaseModel):

    def __init__(self, name):
        self.name = name
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    # converts the user object into a dictionary so we can save it to JSON
    def to_dict(self):
        return {
            "name": self.name,
            "projects": [p.to_dict() for p in self.projects]
        }
