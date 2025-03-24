import requests # type: ignore

API_URL = "https://api.api-ninjas.com/v1/exercises"
API_HEADERS = {"X-Api-Key": "YOUR_API_KEY"}

def get_exercises(muscle_group, equipment=None, difficulty=None, duration=None, body_part=None):
    params = {"muscle": muscle_group}
    
    if equipment:
        params["equipment"] = equipment
    if difficulty:
        params["difficulty"] = difficulty
    if duration:
        params["duration"] = duration
    if body_part:
        params["body_part"] = body_part

    try:
        response = requests.get(API_URL, headers=API_HEADERS, params=params)
        response.raise_for_status()

        exercises = response.json()
        if not exercises:
            print("❗ No exercises found with the given filters. Try different criteria.")
            return []

        return exercises

    except requests.exceptions.RequestException:
        print("⚠️ Error fetching workout data. Please check your internet connection.")
        return []


