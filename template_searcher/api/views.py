import http

from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from core.data_processor import db_handler


# Create your views here.
class GetFormAPIview(APIView):
    """
    Логика работы:
    1. Получить поля и значения (json).
    2. Для каждой пары <название>-<значение> в json определить пару <название>-<тип поля>.
    3. Пересобрать пары в словарь для сравнения с БД.
    4. Провести поиск по БД и найти шаблон, в котором есть все такие поля.
    5. Если таких шаблонов несколько, в приоритете шаблоны с наименьшим количество лишних полей.
    Всё реализовано в core.data_processor.
    """
    def get(self, request, **kwargs):
        return HttpResponse('Hello, friend!')

    def post(self, request, **kwargs):
        data = self.request.data
        if not data:
            return Response(data=data, status=http.HTTPStatus.NOT_FOUND)
        found_template = db_handler(data)
        return found_template
