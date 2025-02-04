from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from data.users import users, save_users

workout_logging_state = {}

async def cmd_log_workout(message: Message):
    user_id = message.from_user.id
    workout_logging_state[user_id] = {"state": "awaiting_type"}
    await message.answer("🟣 Enter workout type:")

async def process_workout_input(message: Message):
    user_id = message.from_user.id
    if user_id not in workout_logging_state:
        return  
    state_data = workout_logging_state[user_id]
    if state_data["state"] == "awaiting_type":
        workout_type = message.text.strip()
        state_data["workout_type"] = workout_type
        state_data["state"] = "awaiting_minutes"
        await message.answer("🟣 Enter workout duration (in minutes):")
    elif state_data["state"] == "awaiting_minutes":
        try:
            minutes = float(message.text)
        except ValueError:
            await message.answer("🚫 Invalid input. Please enter a number for minutes.")
            return
        workout_type = state_data.get("workout_type")
        burned_calories = 10 * minutes
        uid = str(user_id)
        if uid not in users:
            await message.answer("🚫 Profile not found. Please set up your profile using /set_profile.")
            workout_logging_state.pop(user_id, None)
            return
        users[uid].setdefault("burned_calories", 0)
        users[uid]["burned_calories"] += burned_calories
        additional_water = 200 * (minutes // 30)
        users[uid].setdefault("logged_water", 0)
        users[uid]["logged_water"] += additional_water
        save_users(users)
        await message.answer(f"✅ Logged workout: '{workout_type}' for {minutes} minutes, burned {burned_calories} kcal.")
        await message.answer(f"🔵 Drink additional water: {additional_water} ml.")
        workout_logging_state.pop(user_id, None)

def register_workout_handlers(dp: Dispatcher):
    dp.message.register(cmd_log_workout, Command("log_workout"))
    dp.message.register(process_workout_input, lambda message: message.from_user.id in workout_logging_state)
