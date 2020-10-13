from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length = 20)
    nickname = models.CharField(max_length = 15)
    email = models.EmailField(max_length= 30)
    password = models.CharField(max_length =  20)

    class Meta:
        db_table = 'users'

