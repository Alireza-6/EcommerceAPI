from rest_framework.authtoken.views import ObtainAuthToken

from authentication.serializers.admin import AdminLoginSerializer


class AdminLoginView(ObtainAuthToken):
    serializer_class = AdminLoginSerializer
