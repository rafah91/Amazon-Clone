# Generated by Django 4.2.5 on 2023-11-26 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_deliveryfee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='phones',
            field=models.IntegerField(),
        ),
    ]
