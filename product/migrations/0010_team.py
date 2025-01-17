# Generated by Django 5.0.6 on 2024-06-16 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_delete_rcentblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='product/team/')),
                ('speciality', models.ManyToManyField(to='product.speciality')),
            ],
        ),
    ]
