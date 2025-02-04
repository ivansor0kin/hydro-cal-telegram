from aiogram import Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command

async def cmd_start(message: Message):

    welcome_text = (
        "Welcome!\n\n"
        "I will help you calculate your daily water and calorie needs and track your workouts and food intake.\n\n"
        "Available commands:\n"
        "/set_profile - Set up your profile\n"
        "/log_water <amount_in_ml> - Log your water intake\n"
        "/log_food <product_name> <grams> - Log your food intake\n"
        "/log_workout <workout_type> <minutes> - Log your workout details\n"
        "/check_progress - Check your daily progress\n\n"
        "To start, please set up your profile first using /set_profile."
    )
    await message.answer(welcome_text)

def register_start_handlers(dp: Dispatcher):
    dp.message.register(cmd_start, Command("start"))
