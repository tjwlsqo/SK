from django.urls import path
from . import views

urlpatterns = [
    path('api/test', views.Gettest.as_view()),

]