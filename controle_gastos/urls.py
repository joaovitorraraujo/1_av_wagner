"""
URL configuration for controle_gastos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contas.views import addTransaction, addCategory, transactions, updateCategory, updateTrasaction, deleteTransaction, deleteCategory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactions/new/', addTransaction, name='new_transactions'),
    path('transactions/update/<int:pk>/', updateTrasaction, name='update_transactions'),
    path('categories/update/<int:pk>/', updateCategory, name='update_categories'),
    path('transactions/delete/<int:pk>/', deleteTransaction, name='delete_transactions'),
    path('categories/delete/<int:pk>/', deleteCategory, name='delete_categories'),
    path('categories/new/', addCategory, name='new_categories'),
    path('', transactions, name='home'),
]
