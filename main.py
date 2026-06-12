import argparse
from services.storage import load_data, save_data
from utils.helpers import print_success, print_error, print_info

# argparse lets us run commands from the terminal like:
# python main.py add-user --name "Alex"
parser = argparse.ArgumentParser(description="Project Management CLI Tool")
parser.add_argument("--debug", action="store_true", help="Show debug info")
subparsers = parser.add_subparsers(dest="command")

# user commands
user_parser = subparsers.add_parser("add-user")
user_parser.add_argument("--name", required=True)

subparsers.add_parser("list-users")

# project commands
project_parser = subparsers.add_parser("add-project")
project_parser.add_argument("--user", required=True)
project_parser.add_argument("--title", required=True)

list_projects_parser = subparsers.add_parser("list-projects")
list_projects_parser.add_argument("--user", required=True)

# task commands
task_parser = subparsers.add_parser("add-task")
task_parser.add_argument("--project", required=True)
task_parser.add_argument("--title", required=True)

complete_parser = subparsers.add_parser("complete-task")
complete_parser.add_argument("--task", required=True)

args = parser.parse_args()

# load the saved data from the JSON file
data = load_data()

# debug mode shows what command is running and how many users are loaded
if args.debug:
    print(f"[debug] command: {args.command}")
    print(f"[debug] {len(data)} user(s) loaded from database")

if args.command == "add-user":
    # check if user already exists before adding
    for user in data:
        if user["name"] == args.name:
            print_error(f"User '{args.name}' already exists.")
            exit()

    data.append({"name": args.name, "projects": []})
    save_data(data)
    print_success(f"User '{args.name}' created!")

elif args.command == "list-users":
    if not data:
        print_info("No users found.")
    else:
        for user in data:
            print_info(f"  - {user['name']}")

elif args.command == "add-project":
    found = False
    for user in data:
        if user["name"] == args.user:
            user["projects"].append({"title": args.title, "tasks": []})
            save_data(data)
            print_success(f"Project '{args.title}' added!")
            found = True
            break

    if not found:
        print_error(f"User '{args.user}' not found.")

elif args.command == "list-projects":
    for user in data:
        if user["name"] == args.user:
            if not user["projects"]:
                print_info("This user has no projects yet.")
            for p in user["projects"]:
                done = sum(1 for t in p["tasks"] if t["completed"])
                total = len(p["tasks"])
                print_info(f"  - {p['title']}  ({done}/{total} tasks completed)")
            break
    else:
        print_error(f"User '{args.user}' not found.")

elif args.command == "add-task":
    for user in data:
        for project in user["projects"]:
            if project["title"] == args.project:
                project["tasks"].append({"title": args.title, "completed": False})
                save_data(data)
                print_success(f"Task '{args.title}' added!")
                exit(0)

    print_error(f"Project '{args.project}' not found.")

elif args.command == "complete-task":
    for user in data:
        for project in user["projects"]:
            for task in project["tasks"]:
                if task["title"] == args.task:
                    task["completed"] = True
                    save_data(data)
                    print_success(f"Task '{args.task}' marked as complete!")
                    exit(0)

    print_error(f"Task '{args.task}' not found.")

else:
    parser.print_help()
