# Generated by Django 4.1 on 2022-08-23 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date'),
        ),
    ]
