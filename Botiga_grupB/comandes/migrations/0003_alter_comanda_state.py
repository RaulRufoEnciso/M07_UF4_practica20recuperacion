# Generated by Django 4.1.6 on 2023-06-12 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comandes', '0002_comanda_idcarrito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='state',
            field=models.BooleanField(),
        ),
    ]
