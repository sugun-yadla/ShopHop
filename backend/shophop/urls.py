from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shophop.urls')),
]
