from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVQXZ"))
    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))
    if request.GET.get('special'):
        characters.extend(list("!@#$%&"))
    password = ""
    for x in range(length):
        password+=random.choice(characters)
    return render(request, "generator/password.html", {'password': password})


def about(request):
    return render(request, "generator/aboutus.html")
