"""Sambad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView

from django.conf import settings
from django.templatetags.static import static as static_tag

from django.contrib import admin

from rest_framework import schemas

urlpatterns = [
    # Include urls here.
    url(r'api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api/core/', include('core.endpoints')),
    url(r'api/$', schemas.get_schema_view()),
    url(settings.ADMIN_URL, admin.site.urls),
    url(r'^(?!(api\/)).*', TemplateView.as_view(template_name="index.html")),
]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
