from django.db import models


class user(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email_id = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
    user_name = models.CharField(max_length=70)
