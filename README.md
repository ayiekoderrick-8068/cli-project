# Project Management CLI Tool

A command-line application for managing users, projects, and tasks with JSON persistence and rich colored terminal output.

---

## Setup Instructions

**Requirements**
- Python 3.14+
- Pipenv

**Installation**

```bash
# Clone the repository
git clone https://github.com/ayiekoderrick-8068/cli-project.git
cd cli-project/project-management-cli

# Install dependencies
pip install pipenv
pipenv install

# Activate the virtual environment
pipenv shell
```

---

## CLI Commands

### Users

| Command | Description |
|--------|-------------|
| `python main.py add-user --name "Name"` | Add a new user |
| `python main.py list-users` | List all users |

### Projects

| Command | Description |
|--------|-------------|
| `python main.py add-project --user "Name" --title "Title"` | Add a project to a user |
| `python main.py list-projects --user "Name"` | List all projects for a user |

### Tasks

| Command | Description |
|--------|-------------|
| `python main.py add-task --project "Title" --title "Task"` | Add a task to a project |
| `python main.py complete-task --task "Task"` | Mark a task as complete |

### Showcase

| Command | Description |
|--------|-------------|
| `python main.py showcase` | Display all users, projects, and tasks in a table |

### Debug Mode

Add `--debug` to any command to see extra runtime info:

```bash
python main.py list-users --debug
```

---

## Features Overview

- **User Management** — Create and list users
- **Project Management** — Attach projects to specific users
- **Task Management** — Add tasks to projects and mark them as complete
- **Showcase Table** — View everything in a clean formatted table with color-coded status
- **JSON Persistence** — All data is saved to `data/database.json` automatically
- **Rich Colored Output** — Green for success, red for errors, cyan for info

---

## Project Structure

```
project-management-cli/
├── data/
│   └── database.json       # Persistent storage
├── models/
│   ├── base.py
│   ├── user.py
│   ├── project.py
│   └── task.py
├── services/
│   └── storage.py          # Load and save data
├── utils/
│   └── helpers.py          # Print helpers and showcase table
├── tests/
│   └── test_project.py
├── main.py                 # CLI entry point
├── Pipfile
└── conftest.py
```

---

## Known Issues

- **Duplicate projects** — Running `add-project` twice with the same title creates duplicates since there is no uniqueness check
- **Task lookup by title** — `add-task` and `complete-task` search by project/task title, so tasks or projects with the same name across different users can cause conflicts
- **No task update** — There is no command to edit or delete a task once it has been added
- **No user deletion** — Users cannot be removed via the CLI; you would need to manually edit `data/database.json`
- **Extra spaces in titles** — Titles with accidental extra spaces are saved as-is and must be matched exactly in subsequent commands
