import http
import re
from math import inf

from rest_framework.response import Response
from tinydb import TinyDB, Query


def validator(expression: str) -> str:
    """
    Принимает значение поля и определяет его тип:
    Email / телефон / дата / текст
    :param expression:
    :return:
    """
    email_pattern = r'\S+@\S+\.\S+'
    telephone_pattern = r'^\+7\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2}$'
    date_pattern1 = r'^\d{4}-\d{2}-\d{2}$'
    date_pattern2 = r'^\d{2}\.\d{2}\.\d{4}$'

    if re.search(email_pattern, expression):
        return 'email'
    elif re.search(telephone_pattern, expression):
        return 'telephone'
    elif (re.search(date_pattern1, expression)
          or re.search(date_pattern2, expression)):
        return 'date'
    else:
        return 'text'


def data_transformer(data: dict[str, str]) -> dict[str, str]:
    """
    Формируем из тела запроса словарь, содержащий все поля и их типы.
    :param data:
    :return:
    """
    # формируем из тела запроса пары: <имя поля>, <значение поля>
    name_value = list()
    for d in data:
        name_value.append([d, data[d]])

    # превращаем пары [<имя поля>, <значение поля>]
    # в словарь, содержащий все поля и их типы
    name_type_dict = dict()
    for nv in name_value:
        name_type_dict[nv[0]] = validator(nv[1])
    return name_type_dict


def db_handler(post_data: dict[str, str]):
    """
    Принимает обработанную информацию из POST-запроса
    и ищет совпадения с ней в БД.
    :param post_data:
    :return:
    """
    db_templates = TinyDB('db_templates.json')
    new_data = data_transformer(data=post_data)
    matches = db_templates.search(
        Query().fragment(new_data)
    )
    if len(matches) == 0:
        return Response(data=post_data, status=http.HTTPStatus.NOT_FOUND)

    # здесь нужно среди всех результатов выбрать тот,
    # в котором меньше всего полей,
    # поскольку по ТЗ нужен "наиболее подходящий" шаблон
    # считаем, что наименее избыточный и есть оптимальный вариант
    fields_number = inf
    for match in matches:
        if len(match) < fields_number:
            result = match
            fields_number = len(match)

    return Response(data=result['template_name'], status=http.HTTPStatus.OK)
