from django.urls import path
from .views import ProductViews, ProductmaterialViews

urlpatterns = [
    path("product/", ProductViews.as_view(), name="product-list"),
    path("product-material/", ProductmaterialViews.as_view(), name="product-material")
]
