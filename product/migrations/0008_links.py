# Generated by Django 5.0.6 on 2024-06-15 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_rcentblog_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facbook', models.URLField(null=True)),
                ('instagramm', models.URLField(null=True)),
                ('twitter', models.URLField(null=True)),
                ('linkidin', models.URLField(null=True)),
            ],
        ),
    ]
