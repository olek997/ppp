from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional
import json

@dataclass
class Place:
    """Модель данных для места"""
    place_id: str
    name: str
    address: str
    latitude: float
    longitude: float
    accuracy: int
    types: str
    website: str
    language: str
    created_at: str = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
    
    def to_dict(self):
        """Конвертирует объект в словарь"""
        return asdict(self)
    
    def to_json(self):
        """Конвертирует объект в JSON"""
        return json.dumps(self.to_dict())

class PlaceManager:
    """Менеджер для работы с местами (вместо БД используем словарь)"""
    
    def __init__(self):
        self.places = {}
        self.next_id = 1
    
    def create(self, place_data: dict) -> Place:
        """Создает новое место"""
        place_id = str(self.next_id)
        self.next_id += 1
        
        # Создаем объект Place с обязательными полями
        place = Place(
            place_id=place_id,
            name=place_data.get('name', ''),
            address=place_data.get('address', ''),
            latitude=place_data.get('latitude', 0.0),
            longitude=place_data.get('longitude', 0.0),
            accuracy=place_data.get('accuracy', 0),
            types=place_data.get('types', ''),
            website=place_data.get('website', ''),
            language=place_data.get('language', '')
        )
        
        self.places[place_id] = place
        return place
    
    def get(self, place_id: str) -> Optional[Place]:
        """Получает место по ID"""
        return self.places.get(place_id)
    
    def update(self, place_id: str, update_data: dict) -> Optional[Place]:
        """Обновляет место"""
        place = self.get(place_id)
        if not place:
            return None
        
        # Обновляем только разрешенные поля
        updatable_fields = ['name', 'address', 'latitude', 'longitude', 
                           'accuracy', 'types', 'website', 'language']
        
        for field in updatable_fields:
            if field in update_data:
                setattr(place, field, update_data[field])
        
        return place
    
    def delete(self, place_id: str) -> bool:
        """Удаляет место"""
        if place_id in self.places:
            del self.places[place_id]
            return True
        return False
    
    def get_all(self) -> list:
        """Получает все места"""
        return list(self.places.values())

# Глобальный экземпляр менеджера
place_manager = PlaceManager()