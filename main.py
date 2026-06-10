import argparse
from services.storage import load_data, save_data
from utils.helpers import print_success, print_error, print_info

parser = argparse.ArgumentParser(description="Project Management CLI Tool")
subparsers = parser.add_subparsers(dest="command")

# Add User
user_parser = subparsers.add_parser("add-user")
user_parser.add_argument("--name", required=True)

# List Users
subparsers.add_parser("list-users")

# Add Project
project_parser = subparsers.add_parser("add-project")
project_parser.add_argument("--user", required=True)
project_parser.add_argument("--title", required=True)

# Add Task
task_parser = subparsers.add_parser("add-task")
task_parser.add_argument("--project", required=True)
task_parser.add_argument("--title", required=True)

# Complete Task
complete_parser = subparsers.add_parser("complete-task")
complete_parser.add_argument("--task", required=True)

# List Projects
list_projects_parser = subparsers.add_parser("list-projects")
list_projects_parser.add_argument("--user", required=True)

args = parser.parse_args()
data = load_data()

if args.command == "add-user":
    if any(u["name"] == args.name for u in data):
        print_error(f"User '{args.name}' already exists.")
    else:
        data.append({"name": args.name, "projects": []})
        save_data(data)
        print_success(f"User '{args.name}' created!")

elif args.command == "list-users":
    if not data:
        print_info("No users found.")
    for user in data:
        print_info(f"- {user['name']}")

elif args.command == "add-project":
    for user in data:
        if user["name"] == args.user:
            user["projects"].append({"title": args.title, "tasks": []})
            save_data(data)
            print_success(f"Project '{args.title}' added to '{args.user}'!")
            break
    else:
        print_error(f"User '{args.user}' not found.")

elif args.command == "list-projects":
    for user in data:
        if user["name"] == args.user:
            if not user["projects"]:
                print_info("No projects found.")
            for project in user["projects"]:
                tasks_done = sum(1 for t in project["tasks"] if t["completed"])
                print_info(f"- {project['title']} ({tasks_done}/{len(project['tasks'])} tasks done)")
            break
    else:
        print_error(f"User '{args.user}' not found.")

elif args.command == "add-task":
    for user in data:
        for project in user["projects"]:
            if project["title"] == args.project:
                project["tasks"].append({"title": args.title, "completed": False})
                save_data(data)
                print_success(f"Task '{args.title}' added to '{args.project}'!")
                exit()
    print_error(f"Project '{args.project}' not found.")

elif args.command == "complete-task":
    for user in data:
        for project in user["projects"]:
            for task in project["tasks"]:
                if task["title"] == args.task:
                    task["completed"] = True
                    save_data(data)
                    print_success(f"Task '{args.task}' marked as complete!")
                    exit()
    print_error(f"Task '{args.task}' not found.")

else:
    parser.print_help()
