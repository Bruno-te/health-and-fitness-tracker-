from data_fetch.workouts import get_exercises # type: ignore
from utils import display_exercises

def workout_tracker():
    while True:
        print("\n💪 [bold cyan]Workout Tracker[/bold cyan]")
        print("1. Search for workout routines")
        print("2. View past workouts (Coming Soon)")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            muscle_group = input("Enter muscle group (e.g., chest, legs, back): ").strip().lower()
            equipment = input("Filter by equipment (e.g., dumbbells, bands) or leave blank: ").strip().lower()
            difficulty = input("Filter by difficulty (easy, moderate, hard) or leave blank: ").strip().lower()
            duration = input("Filter by duration (short, medium, long) or leave blank: ").strip().lower()
            body_part = input("Filter by body part (e.g., abs, arms) or leave blank: ").strip().lower()

            exercises = get_exercises(muscle_group, equipment, difficulty, duration, body_part)
            display_exercises(exercises)

        elif choice == "2":
            print("Workout history feature is under development! 🚧")
        
        elif choice == "3":
            break

        else:
            print("[red]Invalid choice. Please try again.[/red]")
