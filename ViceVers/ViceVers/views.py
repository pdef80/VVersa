from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def reverse(request):
    return render(request, 'reverse.html')