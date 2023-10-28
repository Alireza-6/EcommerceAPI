from django.urls import path

from authentication.views.admin import AdminLoginView

urlpatterns = [
    path("login/", AdminLoginView.as_view())
]
