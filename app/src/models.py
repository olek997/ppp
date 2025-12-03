from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional
import json

@dataclass
class Place:
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
        return asdict(self)
    
    def to_json(self):
        return json.dumps(self.to_dict())

class PlaceManager:
    
    def __init__(self):
        self.places = {}
        self.next_id = 1
    
    def create(self, place_data: dict) -> Place:
        place_id = str(self.next_id)
        self.next_id += 1
        
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
        return self.places.get(place_id)
    
    def update(self, place_id: str, update_data: dict) -> Optional[Place]:
        place = self.get(place_id)
        if not place:
            return None
        
        updatable_fields = ['name', 'address', 'latitude', 'longitude', 
                           'accuracy', 'types', 'website', 'language']
        
        for field in updatable_fields:
            if field in update_data:
                setattr(place, field, update_data[field])
        
        return place
    
    def delete(self, place_id: str) -> bool:
        if place_id in self.places:
            del self.places[place_id]
            return True
        return False
    
    def get_all(self) -> list:
        return list(self.places.values())

place_manager = PlaceManager()