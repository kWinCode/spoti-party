from django.urls import path, include
from .views import index

app_name = 'frontend'

# we specify the routes here and in the react router -> there would be a way to avoid this!
urlpatterns = [
    path('', index, name=''),
    path('join', index),
    path('create', index),
    path('room/<str:roomCode>', index)
]
