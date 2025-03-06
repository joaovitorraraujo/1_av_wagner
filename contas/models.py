from django.db import models

# Create your models here.
class Categoria(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name
    
class Transacao(models.Model):
    

   

    class Meta:

        verbose_name = 'Transacao'
        verbose_name_plural = 'Transacaos'

    def __str__(self):
        pass
