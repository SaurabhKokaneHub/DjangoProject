from django.shortcuts import render, HttpResponse
from .models import Product

def home(request):
    prod= Product.objects.all()
    return render (request, "electronics/home.html", {"prod":prod})

# Create your views here.
