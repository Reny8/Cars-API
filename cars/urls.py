from django.urls import path
# path needs two arguments the endpoint in string format, and the function to execute
from . import views

urlpatterns = [
    path('', views.cars_list),
]