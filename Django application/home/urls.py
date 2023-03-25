from django.urls import path, include
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.home_render, name='home_render'),
]
