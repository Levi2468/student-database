from django.db import models


class Details(models.Model):
    name=models.CharField(max_length=100)
    Roll_no=models.IntegerField(max_length=10)
