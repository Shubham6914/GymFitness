# Generated by Django 5.0.1 on 2024-02-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('select_date', models.DateTimeField(auto_now_add=True)),
                ('login', models.CharField(max_length=40)),
                ('logout', models.CharField(max_length=40)),
                ('trained_by', models.CharField(max_length=40)),
                ('select_workout', models.CharField(max_length=40)),
            ],
        ),
    ]
