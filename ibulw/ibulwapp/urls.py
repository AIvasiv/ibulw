from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('tracker/sign-in/', auth_views.LoginView.as_view(), {'template_name': 'tracker/sign_in.html'}, name='tracker-sign-in'),
    path('tracker/sign-out/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='tracker-sign-out'),
    path('tracker/', views.tracker_home, name='tracker-home'),
    path('tracker/insert_expense/', views.insert_expense, name='insert_expense_item'),
    path('tracker/insert_category/', views.insert_category, name='insert_category_item'),
    path('tracker/admin_panel/', views.open_admin, name='tracker-admin'),
    path('user/', include('ibulwapp.urls')),
    path('', ),
]
