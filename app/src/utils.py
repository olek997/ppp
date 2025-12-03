import requests
from config import Config
import json

class ExternalAPIClient:
    """Клиент для работы с внешним API (имитация)"""
    
    @staticmethod
    def create_place_external(place_data: dict):
        """Имитация запроса к внешнему API для создания места"""
        # В реальном проекте здесь был бы запрос к:
        # https://rahulshettyacademy.com/maps/api/place/add/json
        
        # Имитируем успешный ответ
        mock_response = {
            "status": "OK",
            "place_id": "mock_external_id",
            "scope": "APP",
            "reference": "mock_ref",
            "id": "mock_id"
        }
        
        # Проверяем наличие обязательных полей
        required_fields = ['name', 'address', 'latitude', 'longitude', 
                          'accuracy', 'types', 'website', 'language']
        
        for field in required_fields:
            if field not in place_data:
                return {"status": "ERROR", "message": f"Missing field: {field}"}
        
        return mock_response
    
    @staticmethod
    def get_place_external(place_id: str):
        """Имитация запроса к внешнему API для получения места"""
        # В реальном проекте: GET → https://rahulshettyacademy.com/maps/api/place/get/json
        
        mock_place = {
            "location": {
                "latitude": "-38.383494",
                "longitude": "33.427362"
            },
            "accuracy": 50,
            "name": "Mock Place",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": "shoe park,shop",
            "website": "http://google.com",
            "language": "French-IN"
        }
        
        if not place_id:
            return {"status": "ERROR", "message": "Place ID is required"}
        
        return mock_place
    
    @staticmethod
    def update_place_external(place_id: str, update_data: dict):
        """Имитация запроса к внешнему API для обновления места"""
        # В реальном проекте: PUT → https://rahulshettyacademy.com/maps/api/place/update/json
        
        mock_response = {
            "msg": "Address successfully updated"
        }
        
        return mock_response
    
    @staticmethod
    def delete_place_external(place_id: str):
        """Имитация запроса к внешнему API для удаления места"""
        # В реальном проекте: DELETE → https://rahulshettyacademy.com/maps/api/place/delete/json
        
        mock_response = {
            "status": "OK"
        }
        
        return mock_response

def validate_place_data(data: dict) -> tuple:
    """Валидация данных места"""
    required_fields = ['name', 'address', 'latitude', 'longitude']
    
    missing_fields = []
    for field in required_fields:
        if field not in data or not data[field]:
            missing_fields.append(field)
    
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    
    # Проверка числовых полей
    try:
        float(data['latitude'])
        float(data['longitude'])
    except ValueError:
        return False, "Latitude and longitude must be numbers"
    
    return True, "Validation passed"