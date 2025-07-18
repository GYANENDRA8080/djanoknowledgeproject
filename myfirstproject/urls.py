"""
URL configuration for myfirstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include  # include is imported to allow for including other URL configurations

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myfirstapp.urls')),  # Include the URLs from the myapp application
]

handler404 = 'myfirstapp.views.error_404_view'  # Custom 404 error handler