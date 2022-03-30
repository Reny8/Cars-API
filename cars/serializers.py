# create serializers module and import the following
from rest_framework import serializers
from .models import Car
# create another class that inherits serializer
class CarSerializer(serializers.ModelSerializer):
    # comes with built in functionality for our model
    # helps us to convert json to python and vice versa
    # create a nested class where you define meta (small bits of info)
    # how the data will be sent out
    class Meta:
        model = Car
        field = ['id','make','model','year','price']