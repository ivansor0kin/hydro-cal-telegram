# Telegram Bot for Water & Calorie Tracking

## Запуск локально
1. Установите зависимости:
pip install -r requirements.txt
2. Укажите токен в файле config.py или используйте переменные среды.
3. Запустите бота:
python bot.py

## Запуск в Docker
1. Соберите образ:
docker build -t water-calorie-bot .
2. Запустите контейнер:
docker run -d --name wc-bot water-calorie-bot

## Команды бота
- `/start` - приветствие
- `/set_profile` - настройка профиля
- `/log_water` <количество>
- `/log_food` <продукт>
- `/log_workout` <тип> <время мин>
- `/check_progress` - проверка прогресса
