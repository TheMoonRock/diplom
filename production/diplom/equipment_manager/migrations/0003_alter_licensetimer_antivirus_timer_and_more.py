# Generated by Django 5.0.4 on 2024-06-06 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_manager', '0002_licensetimer_officeequipment_delete_computer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licensetimer',
            name='antivirus_timer',
            field=models.DateTimeField(verbose_name='Таймер Антивируса'),
        ),
        migrations.AlterField(
            model_name='licensetimer',
            name='office_timer',
            field=models.DateTimeField(verbose_name='Таймер Офиса'),
        ),
        migrations.AlterField(
            model_name='licensetimer',
            name='os_timer',
            field=models.DateTimeField(verbose_name='Таймер ОС'),
        ),
    ]
