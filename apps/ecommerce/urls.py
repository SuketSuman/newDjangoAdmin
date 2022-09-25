from django.urls import path
from apps.ecommerce.views import ProductsView

urlpatterns = [
    path("products/", ProductsView.as_view())
]
