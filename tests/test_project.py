import pytest
from models.task import Task
from models.project import Project
from models.user import User
from models.base import BaseModel
from services.storage import load_data, save_data


# --- Task tests ---

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


# --- Project tests ---

def test_project_add_task():
    project = Project("My Project")
    project.add_task(Task("Do something"))
    assert len(project.tasks) == 1


def test_project_to_dict():
    project = Project("Alpha")
    project.add_task(Task("T1"))
    result = project.to_dict()
    assert result["title"] == "Alpha"
    assert len(result["tasks"]) == 1


# --- User tests ---

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


# --- Inheritance tests ---

def test_user_inherits_base_model():
    assert issubclass(User, BaseModel)


def test_project_inherits_base_model():
    assert issubclass(Project, BaseModel)


def test_task_inherits_base_model():
    assert issubclass(Task, BaseModel)


def test_base_model_raises_not_implemented():
    base = BaseModel()
    with pytest.raises(NotImplementedError):
        base.to_dict()


# --- Storage tests ---

def test_save_and_load_data(tmp_path, monkeypatch):
    db = tmp_path / "database.json"
    monkeypatch.setattr("services.storage.DB_FILE", str(db))

    save_data([{"name": "Alex", "projects": []}])
    result = load_data()
    assert result[0]["name"] == "Alex"


def test_load_returns_empty_when_no_file(tmp_path, monkeypatch):
    monkeypatch.setattr("services.storage.DB_FILE", str(tmp_path / "missing.json"))
    assert load_data() == []


def test_load_handles_corrupt_file(tmp_path, monkeypatch):
    db = tmp_path / "database.json"
    db.write_text("not valid json")
    monkeypatch.setattr("services.storage.DB_FILE", str(db))
    assert load_data() == []
