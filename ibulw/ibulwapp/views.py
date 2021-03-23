from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from .models import Expense_Items
from .models import Categories
from .forms import ExpenseForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

@login_required(login_url='/tracker/sign-in/')
def tracker_home(request):
    context = {'expenses_list' : Expense_Items.objects.all()}
    return render(request, 'tracker/tracker_home.html', context)

def list_expenses(request):
    context = {'expenses_list' : Expense_Items.objects.all()}
    return render(request, 'tracker/expenses_list.html', context)

def form_expenses(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = ExpenseForm()
        else:
            expense = Expense_Items.objects.get(pk = id)
            form = ExpenseForm(instance=expense)
        return render(request, 'tracker/expenses_form.html', {'form':form})
    else:
        if id == 0:
            form = ExpenseForm(request.POST)
        else:
            expense = Expense_Items.objects.get(pk = id)
            form = ExpenseForm(request.POST, instance = expense)
        if form.is_valid():
            form.save()
        return redirect('/tracker/')
        
def delete_expenses(request, id):
    expense = Expense_Items.objects.get(pk = id)
    expense.delete()
    return redirect('/tracker/')