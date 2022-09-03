from rest_framework import serializers
from .models import AuthorizeResponse

class AuthorizeSerializer(serializers.ModelSerializer):
     class Meta:
        model   = AuthorizeResponse
        fields  =  '__all__'