"""omandata URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from omandata import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, reverse
from django.shortcuts import redirect

# Define a custom admin URL pattern with the login_required decorator
@login_required
def custom_admin_view(request):
    return redirect(reverse('admin:index'))  # Redirect to the default admin site

urlpatterns = [
    # Custom admin URL pattern
    path('admin/', custom_admin_view, name='custom_admin'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dataentry.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
