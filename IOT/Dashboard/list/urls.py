from django.urls import include, path
from .import views
app_name='list'
urlpatterns = [
    path('',views.data,name='data'),
]