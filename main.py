import argparse
from services.storage import load_data, save_data
from utils.helpers import print_success, print_error, print_info, print_showcase

# argparse lets us run commands from the terminal like:
# python main.py add-user --name "Alex"
parser = argparse.ArgumentParser(description="Project Management CLI Tool")
parser.add_argument("--debug", action="store_true", help="Show debug info")
subparsers = parser.add_subparsers(dest="command")

subparsers.add_parser("showcase")

# user commands
user_parser = subparsers.add_parser("add-user")
user_parser.add_argument("--name", required=True)
user_parser.add_argument("--debug", action="store_true")

list_users_parser = subparsers.add_parser("list-users")
list_users_parser.add_argument("--debug", action="store_true")

# project commands
project_parser = subparsers.add_parser("add-project")
project_parser.add_argument("--user", required=True)
project_parser.add_argument("--title", required=True)
project_parser.add_argument("--debug", action="store_true")

list_projects_parser = subparsers.add_parser("list-projects")
list_projects_parser.add_argument("--user", required=True)
list_projects_parser.add_argument("--debug", action="store_true")

# task commands
task_parser = subparsers.add_parser("add-task")
task_parser.add_argument("--project", required=True)
task_parser.add_argument("--title", required=True)
task_parser.add_argument("--debug", action="store_true")

complete_parser = subparsers.add_parser("complete-task")
complete_parser.add_argument("--task", required=True)
complete_parser.add_argument("--debug", action="store_true")

# search command
search_parser = subparsers.add_parser("search")
search_parser.add_argument("--query", required=True)
search_parser.add_argument("--debug", action="store_true")

# delete commands
delete_user_parser = subparsers.add_parser("delete-user")
delete_user_parser.add_argument("--name", required=True)
delete_user_parser.add_argument("--debug", action="store_true")

delete_project_parser = subparsers.add_parser("delete-project")
delete_project_parser.add_argument("--user", required=True)
delete_project_parser.add_argument("--title", required=True)
delete_project_parser.add_argument("--debug", action="store_true")

delete_task_parser = subparsers.add_parser("delete-task")
delete_task_parser.add_argument("--project", required=True)
delete_task_parser.add_argument("--title", required=True)
delete_task_parser.add_argument("--debug", action="store_true")

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

elif args.command == "showcase":
    print_showcase(data)

elif args.command == "search":
    query = args.query.lower()
    results = []
    for user in data:
        if query in user["name"].lower():
            results.append(f"[User] {user['name']}")
        for project in user["projects"]:
            if query in project["title"].lower():
                results.append(f"[Project] {project['title']} (User: {user['name']})")
            for task in project["tasks"]:
                if query in task["title"].lower():
                    status = "Done" if task["completed"] else "Pending"
                    results.append(f"[Task] {task['title']} (Project: {project['title']}, Status: {status})")
    if results:
        for r in results:
            print_info(r)
    else:
        print_error(f"No results found for '{args.query}'.")

elif args.command == "delete-user":
    for user in data:
        if user["name"] == args.name:
            data.remove(user)
            save_data(data)
            print_success(f"User '{args.name}' deleted!")
            exit(0)
    print_error(f"User '{args.name}' not found.")

elif args.command == "delete-project":
    for user in data:
        if user["name"] == args.user:
            for project in user["projects"]:
                if project["title"] == args.title:
                    user["projects"].remove(project)
                    save_data(data)
                    print_success(f"Project '{args.title}' deleted!")
                    exit(0)
            print_error(f"Project '{args.title}' not found.")
            exit(1)
    print_error(f"User '{args.user}' not found.")

elif args.command == "delete-task":
    for user in data:
        for project in user["projects"]:
            if project["title"] == args.project:
                for task in project["tasks"]:
                    if task["title"] == args.title:
                        project["tasks"].remove(task)
                        save_data(data)
                        print_success(f"Task '{args.title}' deleted!")
                        exit(0)
                print_error(f"Task '{args.title}' not found.")
                exit(1)
    print_error(f"Project '{args.project}' not found.")

else:
    parser.print_help()
