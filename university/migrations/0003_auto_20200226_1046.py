# Generated by Django 3.0.3 on 2020-02-26 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_auto_20200225_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Дата начала курса'),
        ),
    ]
