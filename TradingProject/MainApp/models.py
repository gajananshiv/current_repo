from django.db import models

# Create your models here.
class Csv(models.Model):
    BANKNIFTY=models.CharField(max_length=20)


    OPEN=models.CharField(max_length=20)
    HIGH=models.CharField(max_length=20)
    LOW=models.CharField(max_length=20)
    CLOSE=models.CharField(max_length=20)
    VOLUME=models.CharField(max_length=20)
