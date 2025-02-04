from config import FOOD_API_URL_TEMPLATE, WEATHER_API_KEY, WEATHER_API_URL
import requests

def get_food_info(product_name):
    url = FOOD_API_URL_TEMPLATE.format(product_name)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        products = data.get('products', [])
        if products:
            first_product = products[0]
            return {
                'name': first_product.get('product_name', 'Unknown'),
                'calories': first_product.get('nutriments', {}).get('energy-kcal_100g', 0)
            }
        return None
    print(f"Error: {response.status_code}")
    return None

def get_weather(city):
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    }
    response = requests.get(WEATHER_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        temp = float(data['main']['temp'])
        description = data['weather'][0]['description']
        return temp
    else:
        print(f"Error: {response.status_code}")
        return None
