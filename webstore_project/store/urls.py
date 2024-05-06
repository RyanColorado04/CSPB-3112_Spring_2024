from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('<slug:tag>', views.products, name='products_by_category'),
    path('product/', views.product, name='product'),
]