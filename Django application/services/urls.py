from django.urls import path, include
from . import views
app_name = 'services'

urlpatterns = [
    path('cropsuggestions', views.crop_Suggestions, name='crop_Suggestions'),
    path('croppredictions', views.crop_predictions, name='crop_predictions'),
]
