from data_fetch.nutrition import get_nutrition # type: ignore
from goal_tracker import update_calorie_progress, view_goal_progress
from utils import display_nutrition

def nutrition_tracker():
    while True:
        print("\n--- Nutrition Tracker ---")
        print("1. Log a meal")
        print("2. View calorie goal progress")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            meal = input("Enter your meal (e.g., '1 cup rice and 2 eggs'): ")
            data = get_nutrition(meal)
            display_nutrition(data)
            
            # Add calories to goal tracking
            total_calories = sum(item['calories'] for item in data)
            update_calorie_progress(total_calories)
            print(f"✅ {total_calories} kcal added to your progress!")

        elif choice == "2":
            view_goal_progress()
        
        elif choice == "3":
            break
        
        else:
            print("Invalid choice. Please try again.")

