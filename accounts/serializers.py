from django.contrib.auth..models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'contact_no','gender','birth_date','balance','picture', 'street_address','city', 'postal_code','country']
