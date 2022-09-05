"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include  # include ni chaqirdik
from project import settings  # settingsni chaqirdik
from django.conf.urls.static import static  # djangodan static ni chaqiryapdi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipe.urls'))  # yana path ochdik va blogni ichidagi urls ni qoshib qoydik
]

if settings.DEBUG:                                                                           # DEBUG --> agar proyekt xali yakunlanmagan bo'lsa pasdagi amallar ishlasin
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)           # settings ni ichidagi STATIC_ROOT ni urlpatterns ga qo'shdik
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)             # settiingsni ichidagi MEDIA_ROOT ni urlpatterns ga qo'shdik
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),                        # debug toolbar dan olindi

