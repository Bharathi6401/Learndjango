# Generated by Django 5.1.3 on 2024-11-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_name', models.CharField(max_length=200)),
                ('study_phase', models.CharField(max_length=200)),
                ('sponser_name', models.CharField(max_length=200)),
                ('study_description', models.CharField(max_length=200)),
            ],
        ),
    ]