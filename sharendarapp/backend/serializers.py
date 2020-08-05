from .models import Events
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
