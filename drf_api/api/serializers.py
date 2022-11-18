from rest_framework import serializers
from .models import Marca,Auto


class AutoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = "__all__"  

class MarcaSerializer (serializers.ModelSerializer):
    mark = AutoSerializer(read_only= True, many=True )
    class Meta:
        model = Marca
        fields = '__all__'