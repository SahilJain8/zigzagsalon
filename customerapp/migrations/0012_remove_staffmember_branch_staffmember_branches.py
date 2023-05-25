# Generated by Django 4.2 on 2023-05-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0011_appointment_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffmember',
            name='branch',
        ),
        migrations.AddField(
            model_name='staffmember',
            name='branches',
            field=models.ManyToManyField(to='customerapp.branch'),
        ),
    ]
