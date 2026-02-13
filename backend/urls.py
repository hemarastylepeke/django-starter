from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('voltage_it_labs/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('accounts.urls')),
]
