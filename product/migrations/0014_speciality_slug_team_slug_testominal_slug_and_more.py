# Generated by Django 5.0.6 on 2024-06-18 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_chairs_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='speciality',
            name='slug',
            field=models.SlugField(default='this is not faound', max_length=255, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.SlugField(default='this is not faound', max_length=255, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='testominal',
            name='slug',
            field=models.SlugField(default='this is not faound', max_length=255, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='chairs',
            name='slug',
            field=models.SlugField(default='this is not faound', max_length=255, verbose_name='Slug'),
        ),
    ]