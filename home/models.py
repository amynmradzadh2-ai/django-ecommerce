from django.db import models

class Category(models.Model):
    name = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/%y/%m/%d/')
    discription = models.TextField()
    price = models.FloatField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name



