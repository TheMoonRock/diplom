from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Problems(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name="Пользователь")
    id_request = models.AutoField(primary_key=True, verbose_name="id")
    request_from_date = models.DateField(verbose_name="Дата обращения")
    name_of_problem = models.CharField(max_length=80, verbose_name="Наименование")
    description_of_problem = models.CharField(max_length=256, verbose_name="Описание")
    STATUS_CHOICES = (
        ('Открыта', 'Открыта'),
        ('В работе', 'В работе'),
        ('Выполнена', 'Выполнена'),
        ('Отклонена', 'Отклонена'),
        ('Ожидает', 'Ожидает'),
        ('На доработку', 'На доработку'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Открыта', blank=True, verbose_name="Статус")
    date_of_finish = models.DateField(null=True, blank=True, verbose_name="Дата завершения")

    def __str__(self):
        return f'{self.id_request} {self.request_from_date} {self.name_of_problem} {self.description_of_problem}'
