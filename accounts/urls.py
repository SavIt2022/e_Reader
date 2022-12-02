from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('school_admin/', views.school_admin, name='school_admin'),
    path('publisher/', views.admin, name='publisher'),
    path('student/', views.admin, name='student'),]
  
   