from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from data.users import users, save_users

water_logging_state = {}

async def cmd_log_water(message: Message):
    user_id = message.from_user.id
    water_logging_state[user_id] = True
    await message.answer("🔵 Enter amount of consumed water (in ml):")

async def process_water_input(message: Message):
    user_id = message.from_user.id
    if user_id not in water_logging_state:
        return
    try:
        amount = float(message.text)
    except ValueError:
        await message.answer("🚫 Invalid input. Please enter a number for water amount.")
        return
    uid = str(user_id)
    if uid not in users:
        await message.answer("🚫 Profile not found. Please set up your profile using /set_profile.")
        water_logging_state.pop(user_id, None)
        return
    users[uid].setdefault("logged_water", 0)
    users[uid]["logged_water"] += amount
    save_users(users)
    await message.answer(f"✅ Logged: {amount} ml water.")
    await message.answer(f"🔵 Total water consumed: {users[uid]['logged_water']} ml.")
    water_logging_state.pop(user_id, None)

def register_water_handlers(dp: Dispatcher):
    dp.message.register(cmd_log_water, Command("log_water"))
    dp.message.register(process_water_input, lambda message: message.from_user.id in water_logging_state)
