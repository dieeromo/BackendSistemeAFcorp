from rest_framework import serializers
from .models import Cliente
from users.models import User

class ClienteSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_name', read_only=True)
    class Meta:
        model = Cliente
        fields = "__all__" 


