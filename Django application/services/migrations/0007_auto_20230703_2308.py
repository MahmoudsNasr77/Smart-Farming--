# Generated by Django 3.2.16 on 2023-07-03 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20230623_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='croppredictions',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='croppredictions',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='waterpredictions',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='waterpredictions',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]