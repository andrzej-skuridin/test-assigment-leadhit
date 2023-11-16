# test-assigment-leadhit
Тестовое задание для соискателя в LeadHit

### Разработчик:
Андрей Скуридин

### Техническое задание:
https://docs.google.com/document/d/1fMFwPBs53xzcrltEFOpEG4GWTaQ-5jvVLrNT6_hmC7I/edit?pli=1

или в корне проекта в формате PDF.


### Установка (Windows OS):
Клонировать репозиторий, находящийся по адресу:

```
https://github.com/andrzej-skuridin/test-assignment-leadhit.git
```

Создать виртуальное окружение:

```
python -m venv venv
```

Активировать виртуальное окружение:

```
source venv/scripts/activate
```

Обновить pip:

```
python -m pip install --upgrade pip
```

Перейти в командной строке в \template_searcher:
```
cd template_searcher
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```


### Тестирование:
В проекте имеются тестовые запросы к БД. С их помощью можно проверить, что:

1) Правильно находятся в базе шаблоны по единственному полю и выбираются шаблоны с минимальным количеством лишних полей (в тестовом варианте без лишних полей).
2) При ненахождении подходящего шаблона выводится входная информация согласно ТЗ.

Для запуска тестовых скриптов:
```
python manage.py test
```
