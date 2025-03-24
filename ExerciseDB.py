import requests # type: ignore

API_URL = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/chest"
API_HEADERS = {
    "X-RapidAPI-Key": "EXERCISEDB_KEY",
    "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}

response = requests.get(API_URL, headers=API_HEADERS)
if response.status_code == 200:
    exercises = response.json()
    for exercise in exercises[:3]:  # Display 3 sample exercises
        print(f"{exercise['name']} - {exercise['target']}")
else:
    print(f"Error: {response.status_code}")
