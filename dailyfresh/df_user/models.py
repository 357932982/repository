from django.db import models


class UserInfo(models.Model):
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=40)
    user_email = models.CharField(max_length=30)
    receiver = models.CharField(max_length=20)
    receiver_address = models.CharField(max_length=100)
    receiver_post = models.CharField(max_length=10)
    receiver_phone = models.CharField(max_length=11)

