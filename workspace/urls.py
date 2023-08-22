"""
URL configuration for workspace project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import MainView

urlpatterns = [
    path('admin/', include('admin.urls')),
    path('search/', include('search.urls')),
    path('notice/', include('notice.urls')),
    path('neulhajang/', include('neulhajang.urls')),
    path('neulhaerang/', include('neulhaerang.urls')),
    path('mypage/', include('mypage.urls')),
    path('main/', include('main.urls')),
    path('member/', include('member.urls')),
    path('customer-center/', include('customer_center.urls')),
    path('static_app/', include('static_app.urls')),
    path('neulhaerang_review/', include('neulhaerang_review.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



