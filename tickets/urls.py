from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_ticket, name='submit_ticket'),
    path('', views.ticket_list, name='ticket_list'),
    path('register/', views.register, name='register'),
]