from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    symbols = User.objects.all()
    print(symbols)
    return render(request, "home.html", {"symbols": symbols})