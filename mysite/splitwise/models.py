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

    def __str__(self):
        return self.username


class Expenses(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='expenses')
    name = models.CharField(max_length=255, unique=False)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='created_expenses', default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    members = models.ManyToManyField(Users, related_name='participated_expenses')

