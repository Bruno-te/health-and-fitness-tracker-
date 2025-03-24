import requests # type: ignore

API_URL = "https://trackapi.nutritionix.com/v2/natural/nutrients"
API_HEADERS = {
    "x-app-id": "NUTRITIONIX",
    "x-app-key": "NINJA",
    "Content-Type": "application/json"
}

data = {
    "query": "1 cup rice and 2 eggs"
}

response = requests.post(API_URL, headers=API_HEADERS, json=data)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
