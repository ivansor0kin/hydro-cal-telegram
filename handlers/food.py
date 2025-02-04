from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from data.users import users, save_users
from utils.api import get_food_info

food_logging_state = {}

async def cmd_log_food(message: Message):
    user_id = message.from_user.id
    food_logging_state[user_id] = {"state": "awaiting_product"}
    await message.answer("🟡 Enter product name:")

async def process_food_input(message: Message):
    user_id = message.from_user.id
    if user_id not in food_logging_state:
        return  # Not in food logging mode.
    state_data = food_logging_state[user_id]
    if state_data["state"] == "awaiting_product":
        product_name = message.text.strip()
        state_data["product_name"] = product_name
        state_data["state"] = "awaiting_grams"
        await message.answer("🟡 Enter amount (in grams):")
    elif state_data["state"] == "awaiting_grams":
        try:
            grams = float(message.text)
        except ValueError:
            await message.answer("🚫 Invalid input. Please enter a number for grams.")
            return
        product_name = state_data.get("product_name")
        food_data = get_food_info(product_name)
        if food_data is None:
            await message.answer("🚫 Could not find product information.")
            food_logging_state.pop(user_id, None)
            return
        calories_per_100g = food_data.get("calories", 0)
        calories = (calories_per_100g * grams) / 100
        uid = str(user_id)
        if uid not in users:
            await message.answer("🚫 Profile not found. Please set up your profile using /set_profile.")
            food_logging_state.pop(user_id, None)
            return
        users[uid].setdefault("logged_calories", 0)
        users[uid]["logged_calories"] += calories
        save_users(users)
        await message.answer(f"✅ Logged: {calories:.2f} kcal for {grams}g of '{product_name}'.")
        food_logging_state.pop(user_id, None)

def register_food_handlers(dp: Dispatcher):
    dp.message.register(cmd_log_food, Command("log_food"))
    dp.message.register(process_food_input, lambda message: message.from_user.id in food_logging_state)
