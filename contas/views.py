from django.shortcuts import get_object_or_404, redirect, render

from contas.models import Category, Transaction
from .form import TransactionForm,CategoryForm


def addTransaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = TransactionForm()

    
    categories = Category.objects.all()

    return render(request, 'contas/add_transaction.html', {'form': form, 'categories': categories})



def addCategory(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_transactions') 
    else:
        form = CategoryForm()

    return render(request, 'contas/add_category.html', {'form':form})



def transactions(request):
    data = {'transactions': Transaction.objects.all()}
    return render(request, 'contas/transactions.html', data)



def updateTrasaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == "POST":
        
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = TransactionForm(instance=transaction)

    
    categories = Category.objects.all()
    return render(request, 'contas/add_transaction.html', {'form': form, 'categories': categories})

def deleteTransaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return redirect('home')