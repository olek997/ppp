from flask import request, jsonify
from .models import place_manager
from .utils import validate_place_data, ExternalAPIClient
import json

def register_routes(app):
    
    @app.route('/entity', methods=['POST'])
    def create_entity():
       
        try:
            data = request.get_json()
            
            if not data:
                return jsonify({
                    "status": "ERROR",
                    "message": "No data provided"
                }), 400
            
            is_valid, message = validate_place_data(data)
            if not is_valid:
                return jsonify({
                    "status": "ERROR",
                    "message": message
                }), 400
            
            place = place_manager.create(data)
            
            external_response = ExternalAPIClient.create_place_external(data)
            
            response_data = {
                "status": "OK",
                "message": "Place created successfully",
                "place_id": place.place_id,
                "external_api_response": external_response,
                "place": place.to_dict()
            }
            
            return jsonify(response_data), 201
            
        except Exception as e:
            return jsonify({
                "status": "ERROR",
                "message": f"Internal server error: {str(e)}"
            }), 500
    
    @app.route('/entity/<string:place_id>', methods=['GET'])
    def get_entity(place_id):
      
        try:
            place = place_manager.get(place_id)
            
            if not place:
                return jsonify({
                    "status": "ERROR",
                    "message": f"Place with ID {place_id} not found"
                }), 404
            
            external_response = ExternalAPIClient.get_place_external(place_id)
            
            response_data = {
                "status": "OK",
                "place": place.to_dict(),
                "external_api_response": external_response
            }
            
            return jsonify(response_data), 200
            
        except Exception as e:
            return jsonify({
                "status": "ERROR",
                "message": f"Internal server error: {str(e)}"
            }), 500
    
    @app.route('/entity/<string:place_id>', methods=['PUT'])
    def update_entity(place_id):
        
        try:
            data = request.get_json()
            
            if not data:
                return jsonify({
                    "status": "ERROR",
                    "message": "No data provided for update"
                }), 400
            
            updated_place = place_manager.update(place_id, data)
            
            if not updated_place:
                return jsonify({
                    "status": "ERROR",
                    "message": f"Place with ID {place_id} not found"
                }), 404
            
            external_response = ExternalAPIClient.update_place_external(place_id, data)
            
            response_data = {
                "status": "OK",
                "message": "Place updated successfully",
                "place": updated_place.to_dict(),
                "external_api_response": external_response
            }
            
            return jsonify(response_data), 200
            
        except Exception as e:
            return jsonify({
                "status": "ERROR",
                "message": f"Internal server error: {str(e)}"
            }), 500
    
    @app.route('/entity/<string:place_id>', methods=['DELETE'])
    def delete_entity(place_id):
        """
        DELETE /entity/{id} - удаление записи места
        Пример: DELETE /entity/1
        """
        try:
            place = place_manager.get(place_id)
            
            if not place:
                return jsonify({
                    "status": "ERROR",
                    "message": f"Place with ID {place_id} not found"
                }), 404
            
            deleted = place_manager.delete(place_id)
            
            if not deleted:
                return jsonify({
                    "status": "ERROR",
                    "message": f"Failed to delete place with ID {place_id}"
                }), 500
            
            external_response = ExternalAPIClient.delete_place_external(place_id)
            
            response_data = {
                "status": "OK",
                "message": f"Place with ID {place_id} deleted successfully",
                "external_api_response": external_response
            }
            
            return jsonify(response_data), 200
            
        except Exception as e:
            return jsonify({
                "status": "ERROR",
                "message": f"Internal server error: {str(e)}"
            }), 500
    
    @app.route('/entities', methods=['GET'])
    def get_all_entities():
        try:
            places = place_manager.get_all()
            
            response_data = {
                "status": "OK",
                "count": len(places),
                "places": [place.to_dict() for place in places]
            }
            
            return jsonify(response_data), 200
            
        except Exception as e:
            return jsonify({
                "status": "ERROR",
                "message": f"Internal server error: {str(e)}"
            }), 500
    
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({
            "status": "OK",
            "message": "API is running",
            "version": "1.0.0"
        }), 200