from django.urls import path
from .views import Detail, NewItems

urlpatterns = [
    path('<int:pk>/', Detail, name='detaill'),
    path('newitem/', NewItems, name='newitems'),
]