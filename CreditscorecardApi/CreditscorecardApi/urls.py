
from django.contrib import admin
from django.urls import path, include
from MY_API import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MY_API.urls')),
    
]
