from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from django.utils import timezone

class User(AbstractUser):
    sourname = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)
    second_name= models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    telephone_number = models.CharField(max_length=30, blank=True)

class Deposit(models.Model):
    number= models.CharField(max_length=30, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.user)


class CreditDeposit(Deposit):
    percent= models.PositiveIntegerField()
    balance = models.PositiveIntegerField()



class DebitDeposit(Deposit):
    balance = models.PositiveIntegerField()



class Card (models.Model):
     number= models.CharField(max_length=30, blank=True)
     deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE)





class Application(models.Model):
    number= models.CharField(max_length=30, blank=True)
    sourname = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)
    second_name= models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    telephone_number = models.CharField(max_length=30, blank=True)
    approved = models.BooleanField(default=False)
    def approve(self):
        self.approved = True
        self.save()


class Transaction(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField()
    def __str__(self):
        return str(self.user)
    class Meta:
        abstract = True
