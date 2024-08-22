from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=255, unique=False)


class Users(models.Model):
    username = models.CharField(max_length=100, unique=False)
    event = models.ForeignKey(Events, on_delete=models.PROTECT)


class Expenses(models.Model):
    name = models.CharField(max_length=255, unique=False)
    price = models.IntegerField()
    event = models.ForeignKey(Events, on_delete=models.PROTECT)


