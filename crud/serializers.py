from rest_framework import serializers
from .models import Crud

class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crud
        fields = ('id', 'title', 'description', 'created_at')  
        read_only_fields = ('created_at',)  
