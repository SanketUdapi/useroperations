from rest_framework import serializers
from .models import Userapp


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userapp
        fields = '__all__'
