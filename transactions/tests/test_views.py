from django.contrib.auth import get_user_model
from django.test import TestCase

from transactions.models import *
from django.urls import reverse

class TransactionViewTest(TestCase):


    @classmethod

    def setUpTestData(cls):
        Diposit.objects.create(user=user_1,balance=0,amount=amount_1=100, timestamp='2010-02-15 00:27:40')
        Diposit.objects.create(user=user_2,balance=0,amount=amount_2=1000,timestamp='2019-02-15 00:28:40')
        Withdrawal.objects.create(user=user_3,balance=100,amount=amount_1=50,timestamp='2010-02-15 00:29:40')
        Withdrawal.objects.create(user=user_4,balance=100,amount=amount_2=250,timestamp='2019-02-15 00:30:40')

   def test_deposit_view(request):
       if form.is_valid():
        form = DepositForm(request.POST or None)
        deposit = form.save(commit=False)
        deposit.user = request.user
        deposit.save()
        deposit.user.account.balance += deposit.amount
        deposit.user.account.save()



   def test_withdrawal_view(request):
    form = WithdrawalForm(request.POST or None, user=request.user)

    if form.is_valid():
        withdrawal = form.save(commit=False)
        withdrawal.user = request.user
        withdrawal.save()
        withdrawal.user.account.balance -= withdrawal.amount
        withdrawal.user.account.save()
