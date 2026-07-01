class Endpoints:
    """Класс для хранения эндпоинтов API"""
    
    ORDERS = "/api/v1/orders"
    ORDER_BY_TRACK = "/api/v1/orders/track"  
    
    @classmethod
    def get_order_by_track(cls, track_number):
        """Возвращает URL для получения заказа по треку с query-параметром"""
        return f"{cls.ORDER_BY_TRACK}?t={track_number}"