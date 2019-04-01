from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = "products/list.html"

    # def get_queryset(self):
    #     products =  super().get_queryset()
    #     return products.filter()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView,self).get_context_data(*args, **kwargs)
    #     print(context)

    #     return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "products/detail.html"
