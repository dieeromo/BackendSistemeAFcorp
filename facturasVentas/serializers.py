from rest_framework import serializers
from .models import FacturasV


class FacturasV_Serializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_name', read_only=True)

    class Meta:
        model = FacturasV
        fields = "__all__"
