# Generated by Django 2.2.6 on 2019-10-29 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20191029_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
