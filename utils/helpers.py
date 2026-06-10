from rich.console import Console

console = Console()

def print_success(msg):
    console.print(f"[green]{msg}[/green]")

def print_error(msg):
    console.print(f"[red]{msg}[/red]")

def print_info(msg):
    console.print(f"[cyan]{msg}[/cyan]")
