# Yatube API

В проекте использованны следующие технологии:
* Бэкэнд - Django
* API фреймворк - Django REST framework
* Авторизация - JWT-токены библиотеки Djoser
* Знания - Курсы Яндекс.Практикум, Google, чаты когорты

### Как запустить проект:

Помолится:
```
https://en.wikipedia.org/wiki/List_of_prayers
```

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/VtlBz/api_final_yatube.git
```
```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv .venv
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```