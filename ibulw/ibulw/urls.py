from django.contrib import admin
from django.urls import path, include
from ibulwapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tracker/sign-in/', auth_views.LoginView.as_view(), {'template_name': 'tracker/sign_in.html'}, name='tracker-sign-in'),
    path('tracker/sign-out/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='tracker-sign-out'),
    path('tracker/', views.tracker_home, name='tracker-home'),
    path('tracker/insert/', views.form_expenses, name='tracker-insert'), #get and post request for insert operation
    path('tracker/insert/<int:id>/', views.form_expenses, name='tracker-update'), #get and post request for update operation
    path('tracker/delete/<int:id>/', views.delete_expenses, name='tracker-delete'), #get and post request for delete operation
    #path('user/', include('ibulwapp.urls'))
]
