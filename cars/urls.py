from django.urls import path
# path needs two arguments the endpoint in string format, and the function to execute
from . import views

urlpatterns = [
    path('', views.cars_list),
    # path for car by id search
    # has to match the name of the parameter for the car_detail function in views
    path('<int:pk>/', views.car_detail)
]