from django.urls import path
from api import views


urlpatterns = [
    path('add/', views.calculate, {'operation': 'add'}, name='add'),
    path('subtract/', views.calculate, {'operation': 'subtract'}, name='subtract'),
    path('multiply/', views.calculate, {'operation': 'multiply'}, name='multiply'),
    path('divide/', views.calculate, {'operation': 'divide'}, name='divide'),
]
