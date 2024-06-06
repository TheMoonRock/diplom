from django.db import models
from django.contrib.auth.models import User

class OfficeEquipment(models.Model):
    id_device = models.AutoField(primary_key=True, verbose_name="ID устройства")
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    category = models.CharField(max_length=50, verbose_name="Категория")
    status = models.CharField(max_length=50, verbose_name="Статус оборудования")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    department = models.CharField(max_length=50, verbose_name="Отдел")
    delivery_date = models.DateField(verbose_name="Дата поставки")

    def __str__(self):
        return f"{self.name} ({self.category})"

class LicenseTimer(models.Model):
    os_timer = models.DurationField(verbose_name="Таймер ОС")
    antivirus_timer = models.DurationField(verbose_name="Таймер Антивируса")
    office_timer = models.DurationField(verbose_name="Таймер Офиса")

    def __str__(self):
        return f"ОС: {self.os_timer}, Антивирус: {self.antivirus_timer}, Офис: {self.office_timer}"
