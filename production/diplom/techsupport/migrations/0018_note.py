# Generated by Django 5.0.4 on 2024-06-19 15:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techsupport', '0017_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_date', models.DateField(verbose_name='Дата записи')),
                ('note_text', models.TextField(verbose_name='Текст записи')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techsupport.problem', verbose_name='Заявка')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Работник')),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметки',
            },
        ),
    ]