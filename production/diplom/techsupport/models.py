from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Problems(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    id_request = models.AutoField(primary_key=True)
    request_from_date = models.DateField()
    name_of_problem = models.CharField(max_length=80)
    description_of_problem = models.CharField(max_length=256)
    STATUS_CHOICES = (
        ('Критично', 'Критично'),
        ('Не критично', 'Не критично'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True)
    date_of_finish = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.id_request} {self.request_from_date} {self.name_of_problem} {self.description_of_problem}'
