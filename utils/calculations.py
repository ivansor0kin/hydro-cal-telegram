from utils.api import get_weather

def calculate_water_goal(weight, activity, city):
    base = weight * 30
    extra_activity = 500 * (activity // 30)
    temp = get_weather(city)
    extra_heat = 500 if (temp is not None and temp > 25) else 0
    return base + extra_activity + extra_heat

def calculate_calorie_goal(weight, height, age, activity):
    base_calories = 10 * weight + 6.25 * height - 5 * age
    extra_activity = activity * 5
    return int(base_calories + extra_activity)
