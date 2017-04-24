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
    """
    author: Meg Ducharme
    """
    class Meta:
        model = Customer
        exclude = ()


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: Meg Ducharme
    """
    class Meta:
        model = PaymentType
        exclude = ()


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductType


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        exclude = ()


class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderProduct
        exclude = ()


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: Gilberto Diaz
    """
    class Meta:
        model = Employee
        exclude = ()


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: Gilberto Diaz
    """
    class Meta:
        model = Department
        exclude = ()


class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: Gilberto Diaz
    """
    class Meta:
        model = Computer
        exclude = ()


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: Gilberto Diaz
    """
    class Meta:
        model = Training
        exclude = ()


class TrainingSessionSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: Gilberto Diaz
    """
    class Meta:
        model = TrainingSession
        exclude = ()
