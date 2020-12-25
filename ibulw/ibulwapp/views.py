from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from .models import Expense_Items
from .models import Categories

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

@login_required(login_url='/tracker/sign-in/')
def tracker_home(request):
    context = {'expenses_list' : Expense_Items.objects.all()}
    return render(request, 'tracker/tracker_home.html', context)

def insert_expense(request:HttpRequest):
    new_expense_item = Expense_Items(content = request.POST['content'])
    new_expense_item.save()
    return redirect('/tracker/')

def insert_category(request:HttpRequest): 
    new_category = Categories(category_name = request.POST['category_name'])
    new_category.save()
    return redirect('/tracker/')

def open_admin(request):
    return render(request, 'admin/add_categories.html', {})
 