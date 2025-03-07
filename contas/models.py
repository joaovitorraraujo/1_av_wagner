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
    title = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    observations = models.TextField(null=True, blank=True)
   
    class Meta:

        verbose_name = 'Transacao'
        verbose_name_plural = 'Transacaos'

    def __str__(self):
        return self.title
