# Generated by Django 4.0.6 on 2022-07-21 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='visit_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 21, 12, 51, 36, 175623)),
        ),
    ]