from django.db import models
from django.contrib.auth.models import User

class Computer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    serial_number = models.CharField(max_length=50)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
