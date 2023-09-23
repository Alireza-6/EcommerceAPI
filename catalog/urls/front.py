from rest_framework.routers import SimpleRouter

from catalog.views.front import CategoryView

router = SimpleRouter()
router.register("categories", CategoryView)
urlpatterns = [
    *router.urls
]
