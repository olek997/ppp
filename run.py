from app.src.app import create_app

app = create_app()

if __name__ == '__main__':
    print("Starting Place Management API...")
    print("API доступен по адресу: http://localhost:5000")
    print("\nДоступные эндпоинты:")
    print("  POST   /entity      - Создать место")
    print("  GET    /entity/{id} - Получить место по ID")
    print("  PUT    /entity/{id} - Обновить место")
    print("  DELETE /entity/{id} - Удалить место")
    print("  GET    /entities    - Получить все места")
    print("  GET    /health      - Проверка здоровья API")
    
    app.run(debug=True, host='0.0.0.0', port=5000)