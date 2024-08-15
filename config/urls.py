from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("suppliers/", include("suppliers.urls", namespace="suppliers")),
    path("products/", include("products.urls", namespace="products")),
    path("users/", include("users.urls", namespace="users")),
]
