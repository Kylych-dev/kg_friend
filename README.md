# kg_friend
quiz project


Технологии

   - Python
   - Django
   - Django REST Framework
   - postgresql
   - decouple
   - venv
   - swagger/redoc
   - logger
   - postman (добавлены колекции для тестов)


Тестирование по темам - Руководство пользователя

Этот сервис предоставляет возможность проходить тестирование по различным темам. <br> 
Пользователи могут зарегистрироваться, авторизоваться и пройти тесты, после чего <br> 
они могут увидеть свои результаты.

Установка

- Клонируйте репозиторий на свой локальный компьютер:
``` bash 
git clone https://github.com/Kylych-dev/kg_friend/
```

- Создайте и активируйте виртуальное окружение:
``` bash
python -m venv venv
source venv/bin/activate
```
- Установите зависимости:
``` bash
pip install -r requirements.txt
```

- Примените миграции:
``` bash
python manage.py migrate
```
- Создайте суперпользователя:
``` bash
python manage.py createsuperuser
```
- Запустите сервер:
``` bash
python manage.py runserver
``` 
- Перейдите по адресу 
http://127.0.0.1:8000/admin/
- войдите с использованием созданного суперпользователя и создайте наборы тестов, вопросы и ответы к вопросам. <br> 

Использование

    Зарегистрируйтесь или войдите в систему.
    После входа в систему вы увидите список доступных тестовых наборов.
    Выберите тестовый набор и пройдите тесты, последовательно отвечая на вопросы.
    После завершения тестирования вы увидите результаты:
        количество правильных и неправильных ответов
        процент правильных ответов

Админка

    В админке Django вы можете управлять пользователями, наборами тестов, вопросами и ответами к вопросам. 
    В разделе наборов тестов вы можете добавлять, редактировать и удалять вопросы и ответы к вопросам.  


## Endpoints

| Endpoint                                                               | Description                                                                                 |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| '`admin/`'                                                             | Admin panel                                                                                 |
| '`swagger/`'                                                           | Swagger Document API endpoints, including parameters, request bodies, and response schemas. |
| '`redoc/`'                                                             | Redoc Document API endpoints, including parameters, request bodies, and response schemas.   |
| '`api/v1/register/`'                                                   | Register a new user                                                                         |
| '`api/v1/login/`'                                                      | User login                                                                                  |
| '`api/v1/logout/`'                                                     | User logout                                                                                 |
| '`api/v1/category-list/`'                                              | Quiz list                                                                                   |
| '`api/v1/submit-test/<int:pk>/`'                                       | start quiz                                                                                  |

Структура проекта специально сделана таким образом чтобы в будущем при улучшении и добавлении кода можно <br> 
было создавать папки и v1 v2 и так далее, аутентифкация находиться отдельно от остального кода, так как <br> 
вряд ли что то поменяется<br> 



├── **<u>api</u>** <br> 
│   ├── **<u>auth</u>** <br> 
│   │   ├── serializers.py <br> 
│   │   └── views.py <br> 
│   ├── route.py <br> 
│   └── **<u>v1</u>** <br> 
│       └── quiz <br> 
│           ├── serializers.py <br> 
│           └── views.py <br> 
├── **<u>apps</u>** <br> 
│   ├── **<u>account</u>** <br> 
│   │   ├── admin.py <br>
│   │   ├── ... <br> 
│   │   └── tests.py <br> 
│   └── **<u>quiz</u>** <br> 
│       ├── admin.py <br> 
│       ├── ... <br>
│       └── views.py <br> 
├── **<u>core</u>** <br> 
│   ├── asgi.py <br> 
│   ├── ... <br>
│   └── yasg.py <br> 

