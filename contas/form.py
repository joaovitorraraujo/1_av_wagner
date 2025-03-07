from django.forms import ModelForm
from .models import Transaction, Category

class TransactionForm(ModelForm):

    class Meta:

        model = Transaction
        fields = ('title','value','category','observations')

class CategoryForm(ModelForm):

    class Meta:

        model = Category
        fields = ('name',)
