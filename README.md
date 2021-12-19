# Пульт охраны банка

Пульт охраны банка, который подключается к удалённой БД, выводит на монитор:
- активные карты доступа в хранилище банка с кодом доступа и датой регистрации карты
- список людей в хранилище на данный момент, вычисляет время нахождения внутри хранилища
- список всех визитов в хранилище каждого пользователя, длительность их пребывания, а также
вычисляет подозрителен ли визит на основании времени пребывания в хранилище



## Установка и запуск
Для работы скрипта необходимы данные для подключения к удаленной БД с визитами
и карточками пропуска сотрудников. Данные для подключения указываются в файле `.env`:
```
DB_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
```
где:
- PASSWORD - пароль
- HOST - хост
- PORT - порт
- NAME - название_БД
- USER - пользователь


Также в `.env` включается отладочный режим работы сайта: `DEBUG` (true/false). По умолчанию
отладочный режим отключен (`DEBUG = False`). Например:
```
DEBUG=true
```

- Скачайте код из репозитория
- Python3 должен быть уже установлен. Используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:

```shell
pip install -r requirements.txt
```

- Запустите сайт командой `python` (`python3`, если есть конфликт с Python2):

```shell
python manage.py runserver 0.0.0.0:8000
```

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).



## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).