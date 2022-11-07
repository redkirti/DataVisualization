from django.urls import path
from .views import my_form

urlpatterns = [
    path('', my_form, name='my-form')
]
