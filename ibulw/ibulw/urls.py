from django.contrib import admin
from django.urls import path
from ibulwapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tracker/sign-in/', auth_views.LoginView.as_view(), {'template_name': 'tracker/sign_in.html'}, name='tracker-sign-in'),
    path('tracker/sign-out/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='tracker-sign-out'),
    path('tracker/', views.tracker_home, name='tracker-home'),
]
