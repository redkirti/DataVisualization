from django.urls import path
from .views import my_form, welcome

urlpatterns = [
    path('start', my_form, name='my-form'),
    path('', welcome, name='wel-come')
]
