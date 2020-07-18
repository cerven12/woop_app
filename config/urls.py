"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from rest_framework import routers
from config import settings
from rest_framework.documentation import include_docs_urls

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# ------------------------------------------
# ----            OPEN API             -----
# ------------------------------------------
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# -----------------------------------------
# -----        END POINTS             -----
# -----------------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apiv1.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title='title')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),



    # SWAGGAR
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

# ----------------------------------------
# -----        DEBUG TOOL BAR        -----
# ----------------------------------------
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/',  include(debug_toolbar.urls))] + urlpatterns

    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

