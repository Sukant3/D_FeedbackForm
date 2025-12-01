from django.contrib import admin
from django.urls import path
from .views import *
from feedback import views 

urlpatterns = [
    # path('', feedback_view, name='feedback'),
    path('feedback/', views.feedback_view, name='feedback'), 
]