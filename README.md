# API Автотест для сервиса "Самокат"

## Описание
Автоматизированный тест для проверки создания заказа самоката и получения информации по треку.

## Сценарий теста
1. Клиент создает заказ через API
2. Сохраняется номер трека заказа
3. Выполняется запрос на получение заказа по треку
4. Проверяется, что код ответа равен 200

## Установка и запуск

### Предварительные требования
- Python 3.8+
- pip

### Установка
```bash
# Клонируйте репозиторий
git clone <https://github.com/nastya0705/api-order-test>
cd api-order-test-python

# Создайте и активируйте виртуальное окружение
python -m venv venv
source venv/bin/activate 

# Установите зависимости
pip install -r requirements.txt
## SQL запросы для проверки базы данных

### Задание 1: Проверка отображения заказа в БД
Вывести список логинов курьеров с количеством их заказов в статусе «В доставке»:

```sql
SELECT 
    c.login, 
    COUNT(o.id) AS orders_in_delivery 
FROM "Couriers" c 
JOIN "Orders" o ON c.id = o."courierId" 
WHERE o."inDelivery" = true 
GROUP BY c.login 
ORDER BY orders_in_delivery DESC;

## Шаг 4: Добавление скриншотов выполнения SQL запросов

Сделайте скриншоты выполнения запросов и добавьте их в папку `screenshots`:

### Для Windows (используйте PowerShell или cmd):

```powershell
# Запустите первый запрос
psql -U morty -d scooter_rent -c "SELECT c.login, COUNT(o.id) AS orders_in_delivery FROM \"Couriers\" c JOIN \"Orders\" o ON c.id = o.\"courierId\" WHERE o.\"inDelivery\" = true GROUP BY c.login ORDER BY orders_in_delivery DESC;"

# Сделайте скриншот результата (Win + Shift + S)
# Сохраните как screenshots/sql_task1.png

# Запустите второй запрос
psql -U morty -d scooter_rent -c "SELECT o.track, CASE WHEN o.finished = true THEN 2 WHEN o.cancelled = true THEN -1 WHEN o.\"inDelivery\" = true THEN 1 ELSE 0 END AS status FROM \"Orders\" o ORDER BY o.track;"

# Сделайте скриншот результата
# Сохраните как screenshots/sql_task2.png