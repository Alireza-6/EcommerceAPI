from rest_framework.routers import SimpleRouter

from catalog.api.views import CategoryView

router = SimpleRouter()
router.register("categories", CategoryView)
urlpatterns = [
    *router.urls
]
