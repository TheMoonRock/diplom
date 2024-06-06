# Generated by Django 5.0.4 on 2024-06-06 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_manager', '0003_alter_licensetimer_antivirus_timer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officeequipment',
            name='status',
            field=models.CharField(choices=[('В работе', 'В работе'), ('В ремонте', 'В ремонте'), ('В запасе', 'В запасе'), ('Списана', 'Списана'), ('Неизвестно', 'Неизвестно'), ('В утилизации', 'В утилизации')], max_length=50, verbose_name='Статус оборудования'),
        ),
    ]