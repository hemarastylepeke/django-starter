from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('voltage_it_labs/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('accounts.urls')),
]
