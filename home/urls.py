
from django.contrib import admin
from django.urls import path,  include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('tasks/', views.tasks, name= 'tasks'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
   
]
