from django.db import models
from datetime import datetime


class Customer(models.Model):
    """
    purpose: expose all customer data
    author: Meg Ducharme
    """
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    date_account_created = models.CharField(max_length=22)
    status = models.IntegerField(default=1)


class PaymentType(models.Model):
    """
    purpose: expose all payment types and add realtionship to Customer class
    author: Meg Ducharme
    """
    account_number = models.IntegerField()
    customer = models.ForeignKey(Customer, related_name='payment_types')


class ProductType(models.Model):
    """
    purpose: create product types table
    author: Meg Ducharme
    """
    name = models.CharField(max_length=70)


class Product(models.Model):
    """
    purpose: expose all product types and add realtionship to product type class
    author: Meg Ducharme
    """
    price = models.FloatField()
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    product_type = models.ForeignKey(ProductType, related_name='products')
    customer = models.ForeignKey(Customer, related_name='products')


class Order(models.Model):
    """
    purpose: expose all order types and add realtionship to PaymentType and Customer classes
    author: Meg Ducharme
    """
    date_order_created = models.DateTimeField(default=datetime.now, blank=True)
    customer = models.ForeignKey(Customer, related_name='orders')
    payment_types = models.ForeignKey(PaymentType, null=True, blank=True, related_name='orders')


class OrderProduct(models.Model):
    """
    purpose: create relationship to show products on an order
    author: Meg Ducharme
    """
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)


class Computer(models.Model):
    """
    purpose: create table to hold computer information
    author: Gilberto Diaz
    """
    purchased_date = models.DateField()
    decommissioned_date = models.DateField(null=True, blank=True)


class Department(models.Model):
    """
    purpose: create table to hold department information
    author: Gilberto Diaz
    """
    name = models.CharField(max_length=100)
    budget = models.FloatField()


class Employee(models.Model):
    """
    purpose: create table to hold employee and create relationship with Computer and Department classes
    author: Gilberto Diaz
    """
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    supervisor = models.IntegerField(default=0)
    department = models.ForeignKey(Department, related_name='employees')
    computer = models.ForeignKey(Computer, related_name='employees')
    customer_support_specialist = models.IntegerField(default=0)


class Training(models.Model):
    """
    purpose: create table to hold training information
    author: Gilberto Diaz
    """
    start_date = models.DateField()
    name = models.CharField(max_length=55)
    end_date = models.DateField(null=True, blank=True)
    max_attendees = models.IntegerField()


class TrainingSession(models.Model):
    """
    purpose: create table to hold relationship between training sessions and employees
    author: Gilberto Diaz
    """
    training = models.ForeignKey(Training)
    employee = models.ForeignKey(Employee)


class CustomerIssue(models.Model):
    """
    purpose: create table to hold customer issues data
    author: Gilberto Diaz
    """
    issue_description = models.TextField()
    resolution_description = models.TextField()
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_resolved = models.DateTimeField(blank=True, null=True)
    order = models.ForeignKey(Order)
