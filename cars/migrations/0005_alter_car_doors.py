# Generated by Django 3.2 on 2022-06-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_doors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.IntegerField(choices=[(2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')]),
        ),
    ]