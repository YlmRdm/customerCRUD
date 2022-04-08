from random import choices
from django.db import models

class Customer(models.Model):  
    cid = models.CharField(max_length=11)
    cname = models.CharField(max_length=100)  
    csurname = models.CharField(max_length=100)
    cphone = models.CharField(max_length=100)
    ccity = models.CharField(max_length=100)
    cdistrict = models.CharField(max_length=100)

    class Meta:  
        db_table = "customer"