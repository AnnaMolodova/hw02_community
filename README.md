# backend_community_homework

[![CI](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml)

### _Cоциальная сеть с авторизацией и комментариями._

Инструменты и стек:
- python
- Django

Реализована часть проекта соцсети:
- Создано и зарегистрировано приложение Posts
- Подключена база данных
- Десять последних записей выводятся на главную страницу
- В админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие
- Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы

### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```sh
pip install -r requirements.txt
```
- В папке с файлом manage.py выполните команду:
```sh
python3 manage.py runserver
```
Автор: Молодова Анна
