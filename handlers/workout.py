from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from data.users import users, save_users

async def cmd_log_workout(message: Message):
    user_id = str(message.from_user.id)
    tokens = message.text.split(maxsplit=2)
    if len(tokens) < 3:
        await message.answer("Usage: /log_workout <workout_type> <minutes>")
        return
    workout_type = tokens[1].strip()
    try:
        minutes = float(tokens[2])
    except ValueError:
        await message.answer("Invalid format for minutes. Please enter a number.")
        return
    burned_calories = 10 * minutes
    if user_id not in users:
        users[user_id] = {}
    users[user_id].setdefault("burned_calories", 0)
    users[user_id]["burned_calories"] += burned_calories
    additional_water = 200 * (minutes // 30)
    users[user_id].setdefault("logged_water", 0)
    users[user_id]["logged_water"] += additional_water
    save_users(users)
    await message.answer(
        f"{workout_type} for {minutes} minutes burned {burned_calories} calories. Additionally, drink {additional_water} ml of water."
    )

def register_workout_handlers(dp: Dispatcher):
    dp.message.register(cmd_log_workout, Command("log_workout"))
