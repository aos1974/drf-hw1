# Generated by Django 4.1 on 2022-08-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='date'),
        ),
    ]
