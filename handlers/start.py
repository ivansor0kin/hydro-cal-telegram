from aiogram import Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command

async def cmd_start(message: Message):
    # keyboard = InlineKeyboardMarkup(inline_keyboard=[
    #     [
    #         InlineKeyboardButton(text="/set_profile", callback_data="set_profile"),
    #         InlineKeyboardButton(text="/log_water", callback_data="log_water")
    #     ],
    #     [
    #         InlineKeyboardButton(text="/log_food", callback_data="log_food"),
    #         InlineKeyboardButton(text="/log_workout", callback_data="log_workout")
    #     ],
    #     [
    #         InlineKeyboardButton(text="/check_progress", callback_data="check_progress")
    #     ]
    # ])
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
    # await message.answer(welcome_text, reply_markup=keyboard)
# async def cmd_button_handler(callback: CallbackQuery):
#     data = callback.data
#     if data == "set_profile":
#         response = "Please set up your profile using the /set_profile command."
#     elif data == "log_water":
#         response = "To log water intake, use: /log_water <amount_in_ml>"
#     elif data == "log_food":
#         response = "To log food intake, use: /log_food <product_name>"
#     elif data == "log_workout":
#         response = "To log a workout, use: /log_workout <workout_type> <minutes>"
#     elif data == "check_progress":
#         response = "To check your progress, use: /check_progress"
#     else:
#         response = "Unknown command."
#     await callback.message.answer(response)
#     await callback.answer()  # Acknowledge the callback

def register_start_handlers(dp: Dispatcher):
    dp.message.register(cmd_start, Command("start"))
    # dp.callback_query.register(cmd_button_handler)
