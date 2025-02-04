import os

# В реальном проекте лучше хранить токен в .env файле и читать его с помощью os.environ
TOKEN = "7942980544:AAGqpq2eHe3jLfsyX4hb74-yGHufB0PBqso"

WEATHER_API_KEY = "d649370277124a97fe59b024a0bad9ef"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Шаблон для запроса к API калорийности еды. Используем форматирование строки.
FOOD_API_URL_TEMPLATE = "https://world.openfoodfacts.org/cgi/search.pl?action=process&search_terms={}&json=true"
