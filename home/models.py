from django.db import models

class Login(models.Model):
    name = models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    age= models.CharField(max_length=50)
    phone= models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name