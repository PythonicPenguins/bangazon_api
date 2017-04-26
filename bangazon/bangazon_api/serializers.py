from django.contrib.auth.models import User, Group
from rest_framework import serializers
from bangazon_api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    purpose: serialize queried data to json for client
    author: Meg Ducharme
    """
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    purpose: serialize queried data to json for client
    author: Meg Ducharme
    """
    class Meta:
        model = Group
        fields = ('url', 'name')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    purpose: serialize queried data to json for client
    author: Meg Ducharme
    """
    class Meta:
        model = Customer
        exclude = ()


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    purpose: serialize queried data to json for client
    author: Meg Ducharme
    """
    class Meta:
        model = PaymentType
        exclude = ()


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    purpose: serialize queried data to json for client
    author: Meg Ducharme
    """
    class Meta:
        model = Product
        exclude = ()


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    purpose: serialize queried data to json for client
    author: Gilberto Diaz
    """
    class Meta:
        model = ProductType
        exclude = ()


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    purpose: serialize queried data to json for client
    author: Gilberto Diaz
    """
    class Meta:
        model = Order
        exclude = ()


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """
    purpose: serialize queried data to json for client
    author: Gilberto Diaz
    """
    class Meta:
        model = Employee
        exclude = ()


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """
    purpose: serialize queried data to json for client
    author: Gilberto Diaz
    """
    class Meta:
        model = Department
        exclude = ()


class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    """
    purpose: serialize queried data to json for client
    author: Gilberto Diaz
    """
    class Meta:
        model = Computer
        exclude = ()


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    """
    purpose: serialize queried data to json for client
    author: Gilberto Diaz
    """
    class Meta:
        model = Training
        exclude = ()

