from django.contrib import admin
from django.urls import path
from webapp import views
urlpatterns = [
    path('', views.CalculatorView.as_view(), name='home'),
    path('api/add/', views.CalculatorView.calculate, {'operation': 'add'}, name='add'),
    path('api/subtract/', views.CalculatorView.calculate, {'operation': 'subtract'}, name='subtract'),
    path('api/multiply/', views.CalculatorView.calculate, {'operation': 'multiply'}, name='multiply'),
    path('api/divide/', views.CalculatorView.calculate, {'operation': 'divide'}, name='divide'),]