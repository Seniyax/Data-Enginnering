import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:

    # OpenWeatherMap API configuration
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
    OPENWEATHER_API_URL = os.getenv('OPENWEATHER_API_URL', 'https://api.openweathermap.org/data/2.5/weather')

    # Database configuration
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = int(os.getenv('DB_PORT', 5432))
    DB_NAME = os.getenv('DB_NAME', 'weather_db')
    DB_USER = os.getenv('DB_USER', 'your_username')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'your_password')

    CITIES = ["London", "New York", "Tokyo", "Colombo", "Sydney"]

settings = Config()
