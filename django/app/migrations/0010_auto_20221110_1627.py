# Generated by Django 3.1.2 on 2022-11-10 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20221110_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circuit',
            name='last_winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pilot'),
        ),
    ]
