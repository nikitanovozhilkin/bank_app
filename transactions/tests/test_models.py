from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Diposit

User = get_user_model()


class DipositTest(TestCase):
    """ Test module for Diposit model """
    def setUp(self):
        user_1 = User.objects.create(username='user #1')
        user_2 = User.objects.create(username='user #2')
        amount_1= 1000000
        amount_2= 2000000
        Diposit.objects.create(user=user_1,amount=amount_1,timestamp='2010-02-15 00:27:40')
        Diposit.objects.create(user=user_2,amount=amount_2,timestamp='2019-02-15 00:27:40')
        
class WithdrawalTest(TestCase):
    """ Test module for Diposit model """
    def setUp(self):
        user_1 = User.objects.create(username='user #1')
        user_2 = User.objects.create(username='user #2')
        amount_1= 999999
        amount_2= 1999999
        Withdrawal.objects.create(user=user_1,amount=amount_1,timestamp='2010-03-15 00:27:40')
        Withdrawal.objects.create(user=user_2,amount=amount_2,timestamp='2019-03-15 00:27:40')
