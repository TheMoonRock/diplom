# Generated by Django 5.0.4 on 2024-06-13 05:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('equipment_manager', '0008_remove_officeequipment_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officeequipment',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group', to_field='name', verbose_name='Отдел'),
        ),
    ]
