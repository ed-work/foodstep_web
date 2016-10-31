from rest_framework import routers

from .core import views as core_views
from .recipe import views as recipe_views


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'recipes', recipe_views.RecipeViewset)
router.register(r'users', core_views.UserViewset)

urlpatterns = router.urls
