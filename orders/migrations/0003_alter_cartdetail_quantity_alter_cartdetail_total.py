# Generated by Django 4.2.5 on 2023-11-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_cart_status_alter_cartdetail_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cartdetail',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
