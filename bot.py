import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import TOKEN
from handlers.start import register_start_handlers
from handlers.profile import register_profile_handlers
from handlers.water import register_water_handlers
from handlers.food import register_food_handlers
from handlers.workout import register_workout_handlers
from handlers.progress import register_progress_handlers

async def main():
    bot = Bot(token=TOKEN, default_bot_properties={"parse_mode": "HTML"})
    dp = Dispatcher(bot=bot)

    # Устанавливаем список команд (меню) для бота,
    # которое отображается пользователю в виде встроенного меню (квадрат с четырьмя кружками)
    commands = [
        BotCommand(command="set_profile", description="Set up your profile"),
        BotCommand(command="log_water", description="Log water intake"),
        BotCommand(command="log_food", description="Log food intake"),
        BotCommand(command="log_workout", description="Log your workout"),
        BotCommand(command="check_progress", description="Check your progress")
    ]
    await bot.set_my_commands(commands)

    register_start_handlers(dp)
    register_profile_handlers(dp)
    register_water_handlers(dp)
    register_food_handlers(dp)
    register_workout_handlers(dp)
    register_progress_handlers(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
