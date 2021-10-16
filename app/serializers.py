from rest_framework import serializers 
from .models import user
 
 
class userSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = user
        fields = (
                  'first_name',
                  'last_name',
                  'email_id',
                  'password',
                  'user_name')