
from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.urls import reverse
from .models import ad,stock



# Create your views here.
def index(request):
    bank_title="View Account"
    return render(request,'index.html',{'bank_title':bank_title})
    



def add(request):
    return render(request,'add.html')
def withdraw(request):
    return render(request,'withdraw.html')

def withdraw(request):
    return render(request,'withdraw.html')

def login(request):
    return render(request,'login.html')

def account(request):
    ads = ad.objects.all()
    return render(request, 'detail.html',{'ads':ads})

def stocks(request):
    stk = stock.objects.all()
    account_details=[
        {'holder_name':'Aroon', 'account_number':'1234 1234 1234', 'account_type':'Savings', 'account_balance':'Rs.50,000'}
    ]
    context={
        'account_details': account_details,
        'stk': stk
    }
    
    return render(request,'stocks.html',context)

    





