from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

admin_urls = [
    path("admin/catalog/", include(('catalog.urls.admin', 'catalog'), namespace='catalog-admin')),
]

front_urls = [
    path("front/catalog/", include(('catalog.urls.front', 'catalog'), namespace='catalog-front')),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(admin_urls)),
    path('api/', include(front_urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
