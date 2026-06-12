from rich.console import Console
from rich.table import Table

# using rich to print colored messages in the terminal
console = Console()


def print_success(message):
    console.print(f"[green]{message}[/green]")


def print_error(message):
    console.print(f"[red]Error: {message}[/red]")


def print_info(message):
    console.print(f"[cyan]{message}[/cyan]")


def print_showcase(data):
    table = Table(title="Project Management Overview", show_lines=True)
    table.add_column("User", style="bold magenta")
    table.add_column("Project", style="bold cyan")
    table.add_column("Task", style="white")
    table.add_column("Status", style="bold")

    if not data:
        console.print("[yellow]No data to display.[/yellow]")
        return

    for user in data:
        if not user["projects"]:
            table.add_row(user["name"], "-", "-", "-")
            continue
        for project in user["projects"]:
            tasks = project["tasks"]
            if not tasks:
                table.add_row(user["name"], project["title"], "-", "-")
                continue
            for task in tasks:
                status = "[green]Done[/green]" if task["completed"] else "[red]Pending[/red]"
                table.add_row(user["name"], project["title"], task["title"], status)

    console.print(table)
