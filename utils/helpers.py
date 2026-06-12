from rich.console import Console

# using rich to print colored messages in the terminal
console = Console()


def print_success(message):
    console.print(f"[green]{message}[/green]")


def print_error(message):
    console.print(f"[red]Error: {message}[/red]")


def print_info(message):
    console.print(f"[cyan]{message}[/cyan]")
