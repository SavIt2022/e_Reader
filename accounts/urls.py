from . import views
from django.urls import path
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login_student/',views.login_student, name="login_student"),
    path('login_admin/',views.login_admin, name="login_admin"),
    path('login_school_admin/',views.login_school_admin, name="login_school_admin"),

    path('register/', views.registerPage, name="register"),

    path('login/', views.loginPage, name="login"),
    path('student/', views.student, name="student"),
    path('school_admin/', views.school_admin, name="school_admin"),

	path('logout/', views.logoutUser, name="logout"),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),


]