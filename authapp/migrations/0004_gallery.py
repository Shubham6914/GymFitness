# Generated by Django 5.0.1 on 2024-02-14 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_enrollment_due_date_enrollment_paymentstatus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='gallery')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
