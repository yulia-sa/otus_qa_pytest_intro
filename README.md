## Задание

Написать по 5 автотестов на методы каждой из структур данных в Python:
1. List
1. Set
1. Dictionary
1. String

Как минимум один тест для каждой структуры должен быть параметризован.
Для тестов на каждую структуру данных создать отдельный файл.

За основу взять методы, которые есть у структур данных: https://docs.python.org/3.6/tutorial/datastructures.html#tuples-and-sequences

## Установка

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```#!bash

pip install -r requirements.txt

```

## Запуск
```#!bash

$ pytest test_list.py
$ pytest test_set.py
$ pytest test_dict.py
$ pytest test_str.py

```
