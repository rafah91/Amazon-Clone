# Generated by Django 4.2.5 on 2023-12-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name_ar',
            field=models.CharField(max_length=120, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_de',
            field=models.CharField(max_length=120, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=120, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='subtitle_ar',
            field=models.TextField(max_length=500, null=True, verbose_name='Subtitle'),
        ),
        migrations.AddField(
            model_name='product',
            name='subtitle_de',
            field=models.TextField(max_length=500, null=True, verbose_name='Subtitle'),
        ),
        migrations.AddField(
            model_name='product',
            name='subtitle_en',
            field=models.TextField(max_length=500, null=True, verbose_name='Subtitle'),
        ),
    ]
