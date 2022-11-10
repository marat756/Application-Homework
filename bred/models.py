from django.db import models

class Cars(models.Model):
    nomi = models.CharField(max_length=20)
    marka = models.CharField(max_length=30)
    narxi = models.IntegerField()
    rasm = models.CharField(max_length=50)
