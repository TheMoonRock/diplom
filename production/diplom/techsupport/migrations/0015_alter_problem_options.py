# Generated by Django 5.0.4 on 2024-06-17 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techsupport', '0014_rename_problems_problem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
    ]
