import pytest
import allure
import json
from src.api.client import ApiClient

@allure.epic("API тесты")
@allure.feature("Заказы")
class TestOrder:
    """Тестовый класс для проверки заказов"""
    
    @allure.story("Создание и получение заказа")
    @allure.title("Создание заказа и получение информации по треку")
    @allure.description("Тест проверяет создание заказа и получение его данных по трек-номеру")
    def test_create_and_get_order(self):
        """Тест-кейс: Клиент создает заказ и получает информацию по треку"""
        
        # 1. Подготовка данных для заказа
        order_data = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "Москва, ул. Примерная, д. 1",
            "metroStation": 4,
            "phone": "+7 999 123-45-67",
            "rentTime": 5,
            "deliveryDate": "2026-07-01",
            "comment": "Позвоните за 10 минут"
        }
        
        # Инициализация клиента
        client = ApiClient()
        
        with allure.step("Выполнить запрос на создание заказа"):
            create_response = client.create_order(order_data)
            
            # Проверяем, что заказ создан успешно
            assert create_response.status_code == 201, f"Ожидался статус 201, получен {create_response.status_code}"
            
            # Сохраняем трек-номер из поля 'track'
            response_data = create_response.json()
            track_number = response_data.get('track')
            
            # Проверяем, что трек-номер получен
            assert track_number is not None, "Трек-номер не найден в ответе"
            
            allure.attach(
                f"Трек-номер заказа: {track_number}",
                name="Трек-номер",
                attachment_type=allure.attachment_type.TEXT
            )
            
            print(f"✅ Трек-номер получен: {track_number}")
        
        with allure.step("Выполнить запрос на получение заказа по треку"):
            get_response = client.get_order_by_track(track_number)
            
            # Проверяем, что код ответа равен 200
            assert get_response.status_code == 200, (
                f"Ожидался статус 200, получен {get_response.status_code}. "
                f"Ответ: {get_response.text}"
            )
            
            # Проверяем структуру ответа
            order_data_response = get_response.json()
            
            # Проверяем, что в ответе есть поле 'order'
            assert 'order' in order_data_response, "Ответ не содержит поле 'order'"
            
            # Проверяем, что трек совпадает
            order = order_data_response['order']
            assert order.get('track') == track_number, (
                f"Трек в ответе ({order.get('track')}) не совпадает с запрошенным ({track_number})"
            )
            
            allure.attach(
                json.dumps(order_data_response, indent=2, ensure_ascii=False),
                name="Данные заказа",
                attachment_type=allure.attachment_type.JSON
            )
            
            print(f"✅ Заказ с треком {track_number} успешно получен")
            print(f"📦 Статус заказа: {order.get('status')}")
            print(f"👤 Клиент: {order.get('firstName')} {order.get('lastName')}")
    
    @allure.story("Негативные сценарии")
    @allure.title("Получение заказа с несуществующим треком")
    def test_get_order_invalid_track(self):
        """Тест: Ошибка при получении заказа с несуществующим трек-номером"""
        
        client = ApiClient()
        invalid_track = 999999999
        
        with allure.step("Выполнить запрос с несуществующим треком"):
            response = client.get_order_by_track(invalid_track)
            
            # API возвращает 404 Not Found для несуществующего заказа
            assert response.status_code == 404, (
                f"Ожидался статус 404, получен {response.status_code}. "
                f"Ответ: {response.text}"
            )
            
            # Проверяем структуру ошибки
            error_data = response.json()
            
            # Проверяем код ошибки
            assert 'code' in error_data, "Ответ не содержит поле 'code'"
            assert error_data['code'] == 404, f"Ожидался код ошибки 404, получен {error_data['code']}"
            
            # Проверяем сообщение об ошибке
            assert 'message' in error_data, "Ответ не содержит поле 'message'"
            assert "Заказ не найден" in error_data['message'], (
                f"Неожиданное сообщение об ошибке: {error_data['message']}"
            )
            
            allure.attach(
                f"Статус: {response.status_code}, Сообщение: {error_data['message']}",
                name="Ответ с ошибкой",
                attachment_type=allure.attachment_type.TEXT
            )
            
            print(f"✅ Ожидаемая ошибка получена: {error_data['message']}")
    
    @allure.story("Создание заказа")
    @allure.title("Создание заказа с разными данными")
    @pytest.mark.parametrize("first_name, rent_time", [
        ("Анна", 1),
        ("Петр", 3),
        ("Мария", 7),
        ("Екатерина", 5),
    ])
    def test_create_order_with_different_data(self, first_name, rent_time):
        """Параметризованный тест для создания заказов с разными данными"""
        
        order_data = {
            "firstName": first_name,
            "lastName": "Тестов",
            "address": "Москва, Красная площадь, д. 1",
            "metroStation": 1,
            "phone": "+7 999 000-00-00",
            "rentTime": rent_time,
            "deliveryDate": "2026-06-30",
            "comment": f"Тестовый заказ для {first_name}"
        }
        
        client = ApiClient()
        
        with allure.step(f"Создание заказа для {first_name} на {rent_time} суток"):
            response = client.create_order(order_data)
            assert response.status_code == 201, f"Не удалось создать заказ: {response.status_code}"
            
            track = response.json().get('track')
            assert track is not None, "Трек-номер не получен"
            
            allure.attach(
                f"Создан заказ для {first_name}, трек: {track}",
                name="Результат",
                attachment_type=allure.attachment_type.TEXT
            )
            
            print(f"✅ Создан заказ для {first_name}, трек: {track}")
            
            # Проверяем, что заказ можно получить
            get_response = client.get_order_by_track(track)
            assert get_response.status_code == 200, "Не удалось получить созданный заказ"
            
            # Проверяем, что данные совпадают
            order_data_response = get_response.json()
            order = order_data_response.get('order', {})
            assert order.get('firstName') == first_name, f"Имя не совпадает: {order.get('firstName')} != {first_name}"