# Пульт охраны банка

Пульт охраны банка, который подключается к удалённой БД, выводит на монитор:
- активные карты доступа в хранилище банка с кодом доступа и датой регистрации карты
- список людей в хранилище на данный момент, вычисляет время нахождения внутри хранилища
- список всех визитов в хранилище каждого пользователя, длительность их пребывания, а также
вычисляет подозрителен ли визит на основании времени пребывания в хранилище



## Установка и запуск

- Скачайте код
- Python3 должен быть уже установлен. Используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

- Запустите сайт командой `python` (`python3`, если есть конфликт с Python2):

```
python main.py
```

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).



## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).