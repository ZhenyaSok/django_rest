26.1
Задание 1
- Подключен и настроен вывод документации для проекта.
- Для работы с документацией проекта установлена и занесена в requirements библиотека drf-yasg
Задание 2
- Подключена возможность оплаты курсов через https://stripe.com/
- Для работы с запросами вам реализовано обращение к эндпоинтам: создание продукта; создание цены; создание сессии для получения ссылки на оплату.


26.2. 

Задание 1
redis, celery, worker работают

Задание 2
Добавлена асинхронная рассылка писем пользователям об обновлении материалов курса.


Задание 3
С помощью celery-beat реализована фоновая задача, которая проверяет пользователей по дате последнего входа по полю 
last_login
 и, если пользователь не заходил более месяца, блокировать его с помощью флага 
is_active
.
(в модель USER добавлены поля last_login, is_active, в user/tasks.py/deactivate_user() периодическая задача, которая реализует решение из задания 2)



