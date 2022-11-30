from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('register', views.register_user, name='register_user'),
    path('create-post', views.create_post, name='create_post'),


]
