# Generated by Django 2.2.6 on 2019-10-29 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20191029_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='test',
        ),
        migrations.AlterField(
            model_name='team',
            name='end_time',
            field=models.DateTimeField(),
        ),
    ]