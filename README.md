# Проект «Товары на все случаи жизни»
Проект YaMDb
## Описание
Добро пожаловать в проект «Товары на все случаи жизни»! Это простое веб-приложение, разработанное как тестовое задание для собеседования. Приложение позволяет пользователям управлять списком продуктов, включая добавление новых продуктов и просмотр их в таблице.
## Стек использованных технологий
+ Backend: Python 3.9, Django 3.2, Django REST Framework
+ Frontend: HTML, CSS, JavaScript
+ Database: SQLite
+ Image Handling: Pillow

## Запуск проекта
+ Клонируйте репозиторий и перейдите в него с помощью командной строки:
```
git clone git@github.com:Elithabeth2003/project_1.git
cd project_1
```
+ Установите и активируйте виртуальное окружение c учетом версии Python 3.9:

* Если у вас Linux/macOS

    ```
    python3 -m venv env
    source env/bin/activate
    ```

* Если у вас Windows

    ```
    python -m venv venv
    source venv/Scripts/activate
    ```

+ Обновите менеджер пакетов pip:

```
python -m pip install --upgrade pip
```

+ Затем установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

+ Выполняем миграции:

```
python manage.py migrate
```

+ Запускаем проект:

```
python manage.py runserver
```

## Автор

[Сиволапова Елизавета](https://github.com/Elithabeth2003)