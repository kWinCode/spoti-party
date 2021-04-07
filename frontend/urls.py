from django.urls import path, include
from .views import index

# we specify the routes here and in the react router -> there would be a way to avoid this!
urlpatterns = [
    path('', index),
    path('join', index),
    path('create', index),
    path('join/1', index)
]
