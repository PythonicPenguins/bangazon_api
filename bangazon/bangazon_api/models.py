from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    date_account_created = models.CharField(max_length=22)
    status = models.IntegerField(default=1)


class Payment_Type(models.Model):
    account_number = models.IntegerField()
    customer_id = models.ForeignKey(Customer)


class Product_Type(models.Model):
    name = models.CharField(max_length=70)


class Product(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    product_type_id = models.ForeignKey(Product_Type)
    customer_id = models.ForeignKey(Customer)



