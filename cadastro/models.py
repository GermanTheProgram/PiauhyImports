from django.db import models

class Usuario (models.Model):
    nome = models.CharField(max_length=50, null=False)
    email= models.CharField(max_length=50, null=False)
    senha = models.CharField(max_length=20, null=False)
    data_cad= models.DateTimeField (auto_now=True)

    def __str__(self):
        return self.nome