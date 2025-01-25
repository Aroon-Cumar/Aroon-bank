from django.urls import path
from .import views

app_name='bank'

urlpatterns=[
    path("home",views.index,name="index"),
    path("account", views.account, name="account"),
    path("add",views.add,name="add"),
    path("withdraw",views.withdraw,name="withdraw"),
    path("login",views.login,name="login"),
    path("stocks",views.stocks,name="stocks"),
    
]