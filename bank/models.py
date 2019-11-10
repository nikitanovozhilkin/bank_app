from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    sourname = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)
    second_name= models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Bill(models.model):
    number= models.CharField(max_length=30, blank=True)
    owner = models.ForeignKey(User, on_delete=models.Cascade)

    class Meta:
        abstract = True


class CreditBill(Bill):
    percent= models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    dolg= amount + amount * (percent / 100)


class DebitBill(Bill):
    balance= models.PositiveIntegerField()



class Card (models.model):
     number= models.CharField(max_length=30, blank=True)
     bill = models.ForeignKey(Bill, on_delete=models.Cascade)
    

