# Health and Fitness Tracker

## 📋 Project Overview
This Health and Fitness Tracker is a Command-Line Interface (CLI) application designed to help users manage their nutrition and workouts effectively. It utilizes external APIs to fetch workout and nutrition data, allowing users to:

✅ Track calorie consumption and workout progress  
✅ Set weekly fitness and nutrition goals  
✅ Filter workouts by muscle group, equipment, duration, and difficulty  
✅ View progress with clear percentage tracking  
✅ Benefit from faster performance with caching  

---

## 🛠️ Installation and Setup
### Prerequisites
- Python 3.10 or higher
- `requests`, `requests-cache`, and `rich` libraries

### 1. Clone the Repository
```bash
git clone <YOUR_REPOSITORY_URL>
cd health-fitness-tracker
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys
1. Create a `.env` file in the root directory.
2. Add your API keys like this:
```
API_NINJAS_KEY=NINJA
```

### 4. Run the Application
```bash
python main.py
```

---

## 🚀 Usage Guide
### Main Menu Options
1. **Nutrition Tracker**
   - Search for food items and track calorie intake.
2. **Workout Tracker**
   - Filter workouts by muscle group, equipment, difficulty, or duration.
3. **Goal Tracker**
   - Set calorie and workout goals.
   - Track your progress toward weekly targets.
4. **Exit**

### Example Commands
**Tracking Nutrition:**
```
> Nutrition Tracker
Enter food name: Chicken Breast
Calories: 165 kcal per 100g
```

**Tracking Workouts:**
```
> Workout Tracker
Enter muscle group: chest
Filter by equipment: dumbbells
✅ Found 3 workouts!
- Dumbbell Bench Press
- Dumbbell Flys
- Incline Dumbbell Press
```

**Setting Goals:**
```
> Goal Tracker
Set calorie goal: 2000
Set workout goal: 5
✅ Goals updated successfully!
```

**Viewing Progress:**
```
> Goal Tracker
🍽️ Calorie Progress: 70%
💪 Workout Progress: 60%
```

---


