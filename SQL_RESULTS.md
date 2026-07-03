@"
# Результаты выполнения SQL запросов

#Задание 1: Курьеры с заказами в доставке

# Запрос:
SELECT 
    c.login, 
    COUNT(o.id) AS orders_in_delivery 
FROM ""Couriers"" c 
JOIN ""Orders"" o ON c.id = o.""courierId"" 
WHERE o.""inDelivery"" = true 
GROUP BY c.login 
ORDER BY orders_in_delivery DESC;

#Задание 2: Статусы заказов

# Запрос:
SELECT 
    o.track,
    CASE 
        WHEN o.finished = true THEN 2
        WHEN o.cancelled = true THEN -1
        WHEN o.""inDelivery"" = true THEN 1
        ELSE 0 
    END AS status 
FROM ""Orders"" o 
ORDER BY o.track;