from django.urls import path
from . import views

# /products
# /product/1/detail
# /product/new
urlpatterns = [
    path ('', views.index)
]
