from django.shortcuts import render
from django.http import HttpResponse


def landing_page(request):
    return render(request, 'landingpage.html')


def login_page(request):
    return render(request, 'loginpage.html')


def sign_up_page(request):
    return render(request, 'signuppage.html')

