# Generated by Django 3.1.2 on 2022-11-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20221110_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='pilot',
        ),
        migrations.AddField(
            model_name='result',
            name='pilot',
            field=models.ManyToManyField(to='app.Pilot'),
        ),
    ]
