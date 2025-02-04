from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from data.users import users, save_users

async def cmd_log_water(message: Message):
    user_id = str(message.from_user.id)
    tokens = message.text.split()
    if len(tokens) < 2:
        await message.answer("Usage: /log_water <amount_in_ml>")
        return
    try:
        amount = float(tokens[1])
    except ValueError:
        await message.answer("Invalid format for water amount.")
        return
    if user_id not in users:
        users[user_id] = {}
    users[user_id].setdefault("logged_water", 0)
    users[user_id]["logged_water"] += amount
    save_users(users)
    await message.answer(f"Logged: {amount} ml water. Total consumed: {users[user_id]['logged_water']} ml.")

def register_water_handlers(dp: Dispatcher):
    dp.message.register(cmd_log_water, Command("log_water"))
