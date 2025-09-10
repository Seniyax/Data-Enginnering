import datetime
import requests
from config.config import Config


class WeatherExtractor:
    def __init__(self, config: Config):
        self.api_key = config.OPENWEATHER_API_KEY
        self.api_url = config.OPENWEATHER_API_URL
        self.cities = config.CITIES

    def fetch_weather_data(self, city: str) :
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            data = response.json()
            return {
                'city': city,
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'weather_description': data['weather'][0]['description'],
                'timestamp': datetime.datetime.utcnow()
            }
        except requests.RequestException as e:
            print(f"❌Error fetching data for {city}: {e}")
            return None

    def extract_all(self):
        weather_data = []
        for city in self.cities:
            data = self.fetch_weather_data(city)
            if data:
                weather_data.append(data)
        return weather_data
        