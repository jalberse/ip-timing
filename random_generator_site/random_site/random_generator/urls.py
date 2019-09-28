from django.urls import path

from . import views

app_name = 'random_generator'
urlpatterns = [
    path('', views.index, name = 'index'),
]