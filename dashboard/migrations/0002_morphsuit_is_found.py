# Generated by Django 3.1.4 on 2020-12-06 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='morphsuit',
            name='is_found',
            field=models.BooleanField(default=False),
        ),
    ]
