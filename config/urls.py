from django.contrib import admin
from django.urls import path, include

v1_urlpatterns = []

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(v1_urlpatterns)),
]
