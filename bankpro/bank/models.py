from django.db import models


class Bank(models.Model):
    bank_name = models.CharField(max_length=20)
    bank_address = models.CharField(max_length=20)
    services = models.CharField(max_length=20)
    total_customers = models.IntegerField()
    branch_manager = models.CharField(max_length=20)



