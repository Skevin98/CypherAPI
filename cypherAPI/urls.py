"""cypherAPI URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers

from API.views import ArticleViewSet,AuthorViewSet, MediaViewSet, \
    ArticleAdminViewSet, AuthorAdminViewSet, MediaAdminViewSet



from django.conf.urls.static import static

router = routers.SimpleRouter()

router.register('author',AuthorViewSet,basename='author')
router.register('article',ArticleViewSet, basename='article')
router.register('media', MediaViewSet, basename='media')
router.register('admin/author',AuthorAdminViewSet,basename='admin-author')
router.register('admin/article',ArticleAdminViewSet, basename='admin-article')
router.register('admin/media', MediaAdminViewSet, basename='admin-media')

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/',include(router.urls)),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
