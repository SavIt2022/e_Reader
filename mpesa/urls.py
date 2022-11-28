from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('', views.index, name='index'),
    path('daraja/stk-push', views.stk_push_callback, name='mpesa_stk_push_callback'),

]