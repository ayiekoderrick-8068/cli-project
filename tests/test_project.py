import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.task import Task
from models.project import Project
from models.user import User

def test_task_completion():
    task = Task("Testing")
    task.complete()
    assert task.completed is True

def test_task_default_not_completed():
    task = Task("New Task")
    assert task.completed is False

def test_task_to_dict():
    task = Task("My Task")
    d = task.to_dict()
    assert d["title"] == "My Task"
    assert d["completed"] is False

def test_project_add_task():
    project = Project("My Project")
    task = Task("Do something")
    project.add_task(task)
    assert len(project.tasks) == 1

def test_project_to_dict():
    project = Project("Alpha")
    project.add_task(Task("T1"))
    d = project.to_dict()
    assert d["title"] == "Alpha"
    assert len(d["tasks"]) == 1

def test_user_add_project():
    user = User("Alex")
    project = Project("P1")
    user.add_project(project)
    assert len(user.projects) == 1

def test_user_to_dict():
    user = User("Alex")
    user.add_project(Project("P1"))
    d = user.to_dict()
    assert d["name"] == "Alex"
    assert len(d["projects"]) == 1
