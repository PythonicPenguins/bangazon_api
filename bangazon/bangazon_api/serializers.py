from django.contrib.auth.models import User, Group
from rest_framework import serializers
from bangazon_api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        exclude = ()

class Payment_TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment_Type
        exclude = ()

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        exclude = ()

class Product_TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product_Type
        exclude = ()
