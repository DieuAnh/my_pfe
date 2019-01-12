from django.db import models

# Create your models here.
class Barreau(models.Model):
    # a, b, c respectivement sont ...
    a = models.FloatField(default=None, verbose_name='Length of bar (m) - dimension a')
    b = models.FloatField(default=None, verbose_name='Width of bar (m) - dimension b')
    l = models.FloatField(default=None, verbose_name='Height of bar (m) - dimension l')
    # csvfile = models.FileField(null=True, blank=True, default=None, verbose_name='CSV upload (optional)')
    # null=True, blank=True makes the
    csvfile = models.FileField(default=None, verbose_name='CSV upload (optional)')
#
class Plate(models.Model):
    # a, b, c respectivement sont ...
    a = models.FloatField(default=None, verbose_name='Length of plate (m) - dimension a')
    b = models.FloatField(default=None, verbose_name='Width of plate (m) - dimension b')
    l = models.FloatField(default=None, verbose_name='Height of plate (m) - dimension l')
    csvfile = models.FileField(default=None, verbose_name='CSV upload (optional)')
