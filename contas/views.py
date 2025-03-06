from django.shortcuts import render

# Create your views here.
def addTransaction(request):
    return render(request, 'contas/add_transaction.html')

def addCategory(request):
    return render(request, 'contas/add_category.html')

def transactions(request):
    return render(request, 'contas/transactions.html')