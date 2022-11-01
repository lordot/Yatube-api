# API YATUBE
API прокта yatube создан для взаимодействия различных приложений и сервисов с Yatube.
Интерфейс позволяет выполнять все возможные действия с постами, комментами и подписками.
Для использования необходима регистрация на сайте Yatube.

# Установка:

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
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
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
