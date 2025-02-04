from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from data.users import users, save_users

profile_setup_stage = {}

async def cmd_set_profile(message: Message):
    profile_setup_stage[message.from_user.id] = "weight"
    await message.answer("⚪️ Enter your weight (in kg):")

async def process_profile_input(message: Message):
    user_id = str(message.from_user.id)
    stage = profile_setup_stage.get(message.from_user.id)
    if stage is None:
        # Если пользователь не в режиме настройки, этот обработчик не должен срабатывать.
        return
    if stage == "weight":
        try:
            weight = float(message.text)
        except ValueError:
            await message.answer("🚫 Invalid format. Please enter a number for weight.")
            return
        users[user_id] = {"weight": weight}
        profile_setup_stage[message.from_user.id] = "height"
        await message.answer("⚪️ Enter your height (in cm):")
    elif stage == "height":
        try:
            height = float(message.text)
        except ValueError:
            await message.answer("🚫 Invalid format. Please enter a number for height.")
            return
        users[user_id]["height"] = height
        profile_setup_stage[message.from_user.id] = "age"
        await message.answer("⚪️ Enter your age:")
    elif stage == "age":
        try:
            age = int(message.text)
        except ValueError:
            await message.answer("🚫 Invalid format. Please enter a number for age.")
            return
        users[user_id]["age"] = age
        profile_setup_stage[message.from_user.id] = "activity"
        await message.answer("⚪️ How many minutes of activity per day?")
    elif stage == "activity":
        try:
            activity = float(message.text)
        except ValueError:
            await message.answer("🚫 Invalid format. Please enter a number for activity minutes.")
            return
        users[user_id]["activity"] = activity
        profile_setup_stage[message.from_user.id] = "city"
        await message.answer("⚪️ Enter your city:")
    elif stage == "city":
        users[user_id]["city"] = message.text.strip()
        profile_setup_stage.pop(message.from_user.id)
        await message.answer("✅ Profile saved! You can now use commands to log data and check your progress.")
    else:
        await message.answer("🚫 Unknown command. Use /set_profile to start setup.")
    save_users(users)

def register_profile_handlers(dp: Dispatcher):
    dp.message.register(cmd_set_profile, Command("set_profile"))
    dp.message.register(process_profile_input, lambda message: message.from_user.id in profile_setup_stage)
