import json
import os

DATA_FILE = "user_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {"calorie_goal": 2000, "calories_consumed": 0}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def update_calorie_progress(calories):
    data = load_data()
    data["calories_consumed"] += calories
    save_data(data)

def view_goal_progress():
    data = load_data()
    remaining = data["calorie_goal"] - data["calories_consumed"]
    print(f"\n🔎 Calorie Goal Progress:")
    print(f"✔️ Consumed: {data['calories_consumed']} kcal")
    print(f"🎯 Goal: {data['calorie_goal']} kcal")
    print(f"🔥 Remaining: {remaining} kcal")
