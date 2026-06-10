# Project Management CLI Tool

A command-line application for managing users, projects, and tasks with JSON persistence.

## Features
- Add Users
- Add Projects per user
- Add Tasks per project
- Complete Tasks
- List Users and Projects
- JSON Persistence
- Rich colored CLI Output

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Create a user
python main.py add-user --name "Alex"

# List all users
python main.py list-users

# Add a project to a user
python main.py add-project --user "Alex" --title "CLI Tool"

# List projects for a user
python main.py list-projects --user "Alex"

# Add a task to a project
python main.py add-task --project "CLI Tool" --title "Build CLI"

# Mark a task as complete
python main.py complete-task --task "Build CLI"
```

## Testing

```bash
pytest
```

## Project Structure

```
project-management-cli/
├── main.py
├── requirements.txt
├── data/
│   └── database.json
├── models/
│   ├── user.py
│   ├── project.py
│   └── task.py
├── services/
│   └── storage.py
├── tests/
│   └── test_project.py
└── utils/
    └── helpers.py
```
# cli-project
