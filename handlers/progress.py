from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from data.users import users
from utils.calculations import calculate_water_goal, calculate_calorie_goal

async def cmd_check_progress(message: Message):
    user_id = str(message.from_user.id)
    if user_id not in users:
        await message.answer("🚫 Profile not found. Please set up your profile using /set_profile.")
        return
    user_data = users[user_id]
    weight = user_data.get("weight", 0)
    height = user_data.get("height", 0)
    age = user_data.get("age", 0)
    activity = user_data.get("activity", 0)
    city = user_data.get("city", "Unknown")
    water_goal = calculate_water_goal(weight, activity, city)
    user_data["water_goal"] = water_goal
    calorie_goal = calculate_calorie_goal(weight, height, age, activity)
    user_data["calorie_goal"] = calorie_goal
    logged_water = user_data.get("logged_water", 0)
    logged_calories = user_data.get("logged_calories", 0)
    burned_calories = user_data.get("burned_calories", 0)
    water_left = max(water_goal - logged_water, 0)
    calorie_balance = logged_calories - burned_calories
    calorie_left = max(calorie_goal - calorie_balance, 0)
    text = (
        f"📊 PROGRESS:\n\n"
        f"Water:\n"
        f"- Consumed: {logged_water} ml out of {water_goal} ml.\n"
        f"- Remaining: {water_left} ml.\n\n"
        f"Calories:\n"
        f"- Consumed: {logged_calories} kcal out of {calorie_goal} kcal.\n"
        f"- Burned: {burned_calories} kcal.\n"
        f"- Balance: {calorie_balance} kcal.\n"
        f"- Remaining to goal: {calorie_left} kcal."
    )
    await message.answer(text)

def register_progress_handlers(dp: Dispatcher):
    dp.message.register(cmd_check_progress, Command("check_progress"))
