# Generated by Django 5.1.3 on 2024-11-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='age1',
            field=models.IntegerField(default=18),
        ),
    ]
