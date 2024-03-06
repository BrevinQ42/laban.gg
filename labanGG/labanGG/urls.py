"""labanGG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('laban.gg/games', include('games_list.urls', namespace="games_list")),
    path('tournaments/', include('tournaments_list.urls', namespace="tournaments_list")),
    path('admin/', admin.site.urls),
    path("laban.gg/", include("create_tournament.urls"))
    path('log_in/', include('log_in.urls', namespace="log_in")),
    path('register/', include('register.urls', namespace="register")),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
