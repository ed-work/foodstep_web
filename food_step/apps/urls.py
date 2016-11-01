from rest_framework_nested import routers

from .core import views as core_views
from .recipe import views as recipe_views


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'recipes', recipe_views.RecipeViewset)
router.register(r'users', core_views.UserViewset)

recipe_routers = routers.NestedSimpleRouter(router, 'recipes', lookup='recipe')
recipe_routers.register(r'steps', recipe_views.StepViewset,
                        base_name='recipe-steps')
recipe_routers.register(r'ingredients', recipe_views.IngredientViewset,
                        base_name='recipe-ingredients')

urlpatterns = router.urls + recipe_routers.urls
