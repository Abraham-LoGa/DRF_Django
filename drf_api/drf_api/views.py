from api.models import Marca, Auto
from api.serializers import MarcaSerializer, AutoSerializer
from rest_framework import viewsets,generics

class Marcaapi(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class =MarcaSerializer
    serch_fields = ('nombre')

class Autoapi (viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

    