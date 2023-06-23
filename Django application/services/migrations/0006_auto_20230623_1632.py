# Generated by Django 3.2.16 on 2023-06-23 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_waterpredictions_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterpredictions',
            name='actual',
            field=models.DecimalField(decimal_places=7, max_digits=15),
        ),
        migrations.AlterField(
            model_name='waterpredictions',
            name='humidity',
            field=models.DecimalField(decimal_places=7, max_digits=15),
        ),
        migrations.AlterField(
            model_name='waterpredictions',
            name='soilMoisture',
            field=models.DecimalField(decimal_places=7, max_digits=15),
        ),
        migrations.AlterField(
            model_name='waterpredictions',
            name='waterLevel',
            field=models.DecimalField(decimal_places=7, max_digits=15),
        ),
        migrations.AlterField(
            model_name='waterpredictions',
            name='water_loss',
            field=models.DecimalField(decimal_places=7, max_digits=15),
        ),
    ]
