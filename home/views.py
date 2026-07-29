from django.shortcuts import render
from django.views import View
from .models import Product

class HomeViews(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'home/home.html', {"products": products})
