import requests
import os
from dotenv import load_dotenv
from .endpoints import Endpoints

load_dotenv()
# Горобийченко Анастасия 44-я коргота -Финальный проеект- Инженер по тестированию QA
class ApiClient:
    """Клиент для взаимодействия с API сервиса 'Самокат'"""
    
    def __init__(self):
        self.base_url = os.getenv('BASE_URL', ' https://25c4dac2-21fe-4219-b3df-2b0c947f4be3.serverhub.praktikum-services.ru/')
        self.endpoints = Endpoints
        self.session = requests.Session()
    
    def create_order(self, order_data):
        """Создание нового заказа"""
        url = f"{self.base_url}{self.endpoints.ORDERS}"
        response = self.session.post(url, json=order_data)
        return response
    
    def get_order_by_track(self, track_number):
        """Получение заказа по трек-номеру через query-параметр t"""
        url = f"{self.base_url}{self.endpoints.get_order_by_track(track_number)}"
        print(f"🔍 URL запроса: {url}")  
        response = self.session.get(url)
        return response