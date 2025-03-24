from data_fetch.nutrition import get_nutrition # type: ignore
from data_fetch.workouts import get_exercises # type: ignore
from utils import display_nutrition, display_exercises

def nutrition_tracker():
    while True:
        print("\n--- Nutrition Tracker ---")
        print("1. Log a meal")
        print("2. View calorie goal progress (Coming Soon)")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            meal = input("Enter your meal (e.g., '1 cup rice and 2 eggs'): ")
            data = get_nutrition(meal)
            display_nutrition(data)

        elif choice == "2":
            print("Calorie goal tracking is under development! 🚧")
        
        elif choice == "3":
            break
        
        else:
            print("Invalid choice. Please try again.")

def workout_tracker():
    while True:
        print("\n--- Workout Tracker ---")
        print("1. Search for workout routines")
        print("2. View past workouts (Coming Soon)")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            muscle_group = input("Enter muscle group (e.g., chest, legs, back): ").strip().lower()
            exercises = get_exercises(muscle_group)
            display_exercises(exercises)

        elif choice == "2":
            print("Workout history feature is under development! 🚧")
        
        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("\n=== Health & Fitness Tracker ===")
        print("1. Nutrition Tracker")
        print("2. Workout Tracker")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            nutrition_tracker()
        elif choice == "2":
            workout_tracker()
        elif choice == "3":
            print("Goodbye! Stay healthy! 💪")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
