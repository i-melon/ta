from django.db import models

# Create your models here.
class Market(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    businessAccount = models.BooleanField()
    description = models.TextField(max_length=150)
    def __str__(self):
        return self.name
