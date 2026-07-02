@"
-- ============================================
-- SQL запросы для проверки данных в БД
-- Сервис аренды самокатов "Самокат"
-- База данных: scooter_rent
-- Пользователь: morty
-- ============================================

-- ============================================
-- Задание 1: Проверка отображения заказа в БД
-- ============================================
-- Вывести список логинов курьеров с количеством их заказов 
-- в статусе «В доставке» (поле inDelivery = true)

SELECT 
    c.login, 
    COUNT(o.id) AS orders_in_delivery 
FROM ""Couriers"" c 
JOIN ""Orders"" o ON c.id = o.""courierId"" 
WHERE o.""inDelivery"" = true 
GROUP BY c.login 
ORDER BY orders_in_delivery DESC;

-- ============================================
-- Задание 2: Проверка статусов заказов
-- ============================================
-- Вывести все трекеры заказов и их статусы
-- Статусы определяются по правилу:
--   finished = true  → статус 2
--   cancelled = true → статус -1
--   inDelivery = true → статус 1
--   остальные случаи → статус 0

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
"@ | Out-File -FilePath query.sql -Encoding utf8