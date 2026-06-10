class User:
    def __init__(self, name):
        self.name = name
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "name": self.name,
            "projects": [project.to_dict() for project in self.projects]
        }
