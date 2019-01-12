# Generated by Django 2.1.4 on 2019-01-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190109_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barreau',
            name='a',
            field=models.FloatField(default=None, verbose_name='Length of bar (m) - dimension a'),
        ),
        migrations.AlterField(
            model_name='barreau',
            name='b',
            field=models.FloatField(default=None, verbose_name='Width of bar (m) - dimension b'),
        ),
        migrations.AlterField(
            model_name='barreau',
            name='csvfile',
            field=models.FileField(default=None, upload_to='', verbose_name='CSV upload (optional)'),
        ),
        migrations.AlterField(
            model_name='barreau',
            name='l',
            field=models.FloatField(default=None, verbose_name='Height of bar (m) - dimension l'),
        ),
    ]
