# Generated by Django 3.1.2 on 2022-11-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_profile_favourite_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
