# Generated by Django 2.1.4 on 2019-01-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_barreau_plaque'),
    ]

    operations = [
        migrations.AddField(
            model_name='barreau',
            name='csvfile',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
