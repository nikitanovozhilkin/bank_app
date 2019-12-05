from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    sourname = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)
    second_name= models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    telephone_number = models.CharField(max_length=30, blank=True)

class Deposit(models.model):
    number= models.CharField(max_length=30, blank=True)
    owner = models.ForeignKey(User, on_delete=models.Cascade)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.user)


class CreditDeposit(Deposit):
    percent= models.PositiveIntegerField()
    balance = models.PositiveIntegerField()
    dolg= balance + balance * (percent / 100)


class DebitDeposit(Deposit):
    balance = models.PositiveIntegerField()



class Card (models.model):
     number= models.CharField(max_length=30, blank=True)
     deposit = models.ForeignKey(Bill, on_delete=models.Cascade)

class Application(models.model):
    number= models.CharField(max_length=30, blank=True)
    sourname = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)
    second_name= models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    telephone_number = models.CharField(max_length=30, blank=True)
    approved = models.BooleanField(default=False)


class Transaction(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    deposit = models.ForeignKey(Deposit, on_delete=models.Cascade)
    balance = models.ForeignKey(Deposit, on_delete=models.Cascade)

    def __str__(self):
        return str(self.user)
    class Meta:
        abstract = True
class IncomeTransaction (Transaction):
    amount= models.PositiveIntegerField()
    balance =+ amount

class OutcomeTransaction (Transaction):
    amount= models.PositiveIntegerField()
    balance =- amount

