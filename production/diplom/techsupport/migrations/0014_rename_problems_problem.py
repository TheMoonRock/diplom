# Generated by Django 5.0.4 on 2024-06-17 15:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techsupport', '0013_alter_problems_status_delete_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Problems',
            new_name='Problem',
        ),
    ]
