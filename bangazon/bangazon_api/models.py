from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    date_account_created = models.CharField(max_length=22)
    status = models.IntegerField(default=1)


class PaymentType(models.Model):
    account_number = models.IntegerField()
    customer_id = models.ForeignKey(Customer)
