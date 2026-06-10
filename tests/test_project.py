from models.task import Task
from models.project import Project
from models.user import User


def test_task_completion():
    task = Task("Write tests")
    task.complete()
    assert task.completed is True


def test_task_starts_incomplete():
    task = Task("New Task")
    assert task.completed is False


def test_task_to_dict():
    task = Task("My Task")
    result = task.to_dict()
    assert result["title"] == "My Task"
    assert result["completed"] is False


def test_project_add_task():
    project = Project("My Project")
    task = Task("Do something")
    project.add_task(task)
    assert len(project.tasks) == 1


def test_project_to_dict():
    project = Project("Alpha")
    project.add_task(Task("T1"))
    result = project.to_dict()
    assert result["title"] == "Alpha"
    assert len(result["tasks"]) == 1


def test_user_add_project():
    user = User("Alex")
    user.add_project(Project("P1"))
    assert len(user.projects) == 1


def test_user_to_dict():
    user = User("Alex")
    user.add_project(Project("P1"))
    result = user.to_dict()
    assert result["name"] == "Alex"
    assert len(result["projects"]) == 1
