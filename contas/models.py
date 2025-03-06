from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    date = models.DateTimeField()
    description = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    observations = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
   
    class Meta:

        verbose_name = 'Transacao'
        verbose_name_plural = 'Transacaos'

    def __str__(self):
        return self.description
