from rich.console import Console # type: ignore
from rich.table import Table # type: ignore

console = Console()

def display_exercises(exercises):
    if not exercises:
        console.print("[red]No exercises found. Please refine your search.[/red]")
        return

    table = Table(title="Workout Routines")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Type", style="green")
    table.add_column("Equipment", style="yellow")
    table.add_column("Difficulty", style="magenta")

    for exercise in exercises:
        table.add_row(
            exercise.get("name", "N/A"),
            exercise.get("type", "N/A"),
            exercise.get("equipment", "None"),
            exercise.get("difficulty", "N/A")
        )

    console.print(table)
