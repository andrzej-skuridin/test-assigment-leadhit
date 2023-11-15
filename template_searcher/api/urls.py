from django.urls import path

from api.views import GetFormAPIview

urlpatterns = [
    path(
        'get_form/', GetFormAPIview.as_view()
    ),
]
