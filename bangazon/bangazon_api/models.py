from django.db import models


# Create your models here.
class Customer(models.Model):
    """
    author: Meg Ducharme
    """
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    date_account_created = models.CharField(max_length=22)
    status = models.IntegerField(default=1)


class PaymentType(models.Model):
    """
    author: Meg Ducharme
    """
    account_number = models.IntegerField()
    customer_id = models.ForeignKey(Customer)


class Computer(models.Model):
    """
    author: Gilberto Diaz
    """
    purchased_date = models.DateField()
    decommissioned_date = models.DateField()


class Department(models.Model):
    """
    author: Gilberto Diaz
    """
    name = models.CharField(max_length=100)
    budget = models.FloatField()


class Employee(models.Model):
    """
    author: Gilberto Diaz
    """
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    supervisor = models.IntegerField()
    department_id = models.ForeignKey(Department)
    computer_id = models.ForeignKey(Computer)


class Training(models.Model):
    """
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
