from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    return render(request, 'xhome.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin_dashboard')
            elif user is not None and user.is_school_admin:
                login(request, user)
                return redirect('school_admin_dashboard')
            elif user is not None and user.is_publisher:
                login(request, user)
                return redirect('publisher_dashboard')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('courses_list')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin_dashboard.html')

def publisher(request):
    return render(request,'publisher_dashboard.html')


def school_admin(request):
    return render(request,'school_admin-dashboard.html')


def student(request):
    return render(request,'courses_list.html')