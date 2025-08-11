from .models import Crud
from rest_framework import viewsets, permissions
from .serializers import CrudSerializer  # CORREGIDO: nombre coincide con la clase

class CrudViewSet(viewsets.ModelViewSet):
    queryset = Crud.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CrudSerializer
