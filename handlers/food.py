from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from data.users import users, save_users
from utils.api import get_food_info

async def cmd_log_food(message: Message):
    user_id = str(message.from_user.id)
    tokens = message.text.split()
    if len(tokens) < 3:
        await message.answer("Usage: /log_food <product_name> <grams>")
        return
    try:
        grams = float(tokens[-1])
    except ValueError:
        await message.answer("Invalid format for grams. Please enter a number.")
        return
    product_name = " ".join(tokens[1:-1])
    food_data = get_food_info(product_name)
    if food_data is None:
        await message.answer("Could not find product information.")
        return
    calories_per_100g = food_data.get("calories", 0)
    calories = (calories_per_100g * grams) / 100
    if user_id not in users:
        await message.answer("Profile not found. Please set up your profile using /set_profile.")
        return
    users[user_id].setdefault("logged_calories", 0)
    users[user_id]["logged_calories"] += calories
    save_users(users)
    await message.answer(f"Logged: {calories:.2f} kcal for {grams}g of {product_name}.")

def register_food_handlers(dp: Dispatcher):
    dp.message.register(cmd_log_food, Command("log_food"))
