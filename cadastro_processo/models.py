from django.db import models

# Create your models here.

class Planilha(models.Model):
    nome = models.CharField(verbose_name="nome", max_length=200)
    cliente = models.CharField(verbose_name="cliente",max_length=200)
    arquivo = models.FileField(upload_to="planilhas/")

    def __str__(self):
        return "Processo : " + self.nome + "(Cliente :" + self.cliente + ")"



