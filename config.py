import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    API_KEY = 'qaclick123'  # API key из примера
    BASE_URL = 'https://rahulshettyacademy.com/maps/api/place'
    DEBUG = True