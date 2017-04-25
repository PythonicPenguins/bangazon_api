from django.db import models


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
    customer_id = models.ForeignKey(Customer)


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
    product_type_id = models.ForeignKey(ProductType)
    customer_id = models.ForeignKey(Customer)


class Order(models.Model):
    """
    purpose: expose all order types and add realtionship to PaymentType and Customer classes
    author: Meg Ducharme
    """
    date_order_created = models.DateTimeField()
    customer_id = models.ForeignKey(Customer)
    paymentType_id = models.ForeignKey(PaymentType)

class OrderProduct(models.Model):
    """
    purpose: create relationship to show products on an order
    author: Meg Ducharme
    """
    order_id = models.ForeignKey(Order)
    product_id = models.ForeignKey(Product)


class Computer(models.Model):
    """
    purpose: create table to hold computer information
    author: Gilberto Diaz
    """
    purchased_date = models.DateField()
    decommissioned_date = models.DateField()


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
    supervisor = models.IntegerField()
    department_id = models.ForeignKey(Department)
    computer_id = models.ForeignKey(Computer)


class Training(models.Model):
    """
    purpose: create table to hold traning information
    author: Gilberto Diaz
    """
    start_date = models.DateField()
    name = models.CharField(max_length=55)
    end_date = models.DateField()
    max_attendees = models.IntegerField()


class TrainingSession(models.Model):
    """
    author: Gilberto Diaz
    """
    training_id = models.ForeignKey(Training)
    employee_id = models.ForeignKey(Employee)

