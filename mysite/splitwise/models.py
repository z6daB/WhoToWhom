from django.db import models
from django.contrib.auth import get_user_model

# Get the user model
User = get_user_model()


class Events(models.Model):
    title = models.CharField(max_length=255, unique=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=1)


class Users(models.Model):
    username = models.CharField(max_length=100, unique=False)
    event = models.ForeignKey(Events, on_delete=models.PROTECT)


class Expenses(models.Model):
    name = models.CharField(max_length=255, unique=False)
    price = models.IntegerField()
    event = models.ForeignKey(Events, on_delete=models.PROTECT)
