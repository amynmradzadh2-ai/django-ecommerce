from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product, Category


class HomeViews(View):
    def get(self, request):
        query = request.GET.get('q', '')
        products = Product.objects.filter(available=True)
        if query:
            products = products.filter(name__icontains=query)
        categories = Category.objects.all()
        return render(request, 'home/home.html', {"products": products, "query": query, "categories": categories})


class ProductViews(View):
    def get(self, request, product_id, product_slug):
        product = get_object_or_404(Product, id=product_id, slug=product_slug, available=True)
        return render(request, 'home/product_detail.html', {'product': product})


class CategoryViews(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)
        return render(request, 'home/home.html', {'products': products})