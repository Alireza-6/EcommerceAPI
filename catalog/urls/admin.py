from rest_framework.routers import SimpleRouter

from catalog.views.admin import CategoryView

router = SimpleRouter()
router.register('categories', CategoryView, basename='Category')
urlpatterns = [
    *router.urls
]
