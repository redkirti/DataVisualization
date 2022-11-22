from django.urls import path
from .views import my_form, welcome

urlpatterns = [
    #Main App URL
    path('start', my_form, name='my-form'),
    # Welcome Page URL
    path('', welcome, name='wel-come')
]
