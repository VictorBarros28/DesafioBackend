from django.db import models

# Create your models here.

class Processo(models.Model):
    pasta = models.CharField(verbose_name="pasta",max_length=200)
    comarca = models.CharField(verbose_name="comarca",max_length=200)
    uf = models.CharField(verbose_name="uf",max_length=200)
