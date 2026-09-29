from django.urls import path
from home.models import Category

from .  import views

app_name = 'home'
urlpatterns = [
    path('',views.HomeViews.as_view(),name='home'),
    path('products/<int:product_id>/<slug:product_slug>/', views.ProductViews.as_view(), name='product'),
    path('category/<int:category_id>/', views.CategoryViews.as_view(), name='category'),
]