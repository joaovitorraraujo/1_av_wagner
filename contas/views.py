from django.shortcuts import render

# Create your views here.
def myHome(request):
    return render(request, 'contas/home.html')