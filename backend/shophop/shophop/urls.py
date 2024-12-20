"""
URL configuration for shophop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from shophop.views import *
urlpatterns = [
    path('token', get_tokens, name='get-tokens'),
    path('token/refresh', refresh_tokens, name='refresh-tokens'),

    path('products/<str:product>', fetch_products, name='fetch-products'),
    path('products/', get_products_data, name='product-data'),

    path('saved_items', get_saved_items, name='get-saved-items'),
    path('saved_items/add', save_grocery_items, name='save-tracking-list'),
    path('saved_items/delete', delete_saved_items, name='delete-saved-items'),
    path('price_drop_tracking', price_drop_tracker, name='price-drop-tracker'),
]
