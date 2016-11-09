from django.conf.urls import url
from rest_framework_nested import routers
from rest_framework_jwt import views as jwt_views

from .core import views as core_views
from .recipe import views as recipe_views


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'recipes', recipe_views.RecipeViewset)
router.register(r'users', core_views.UserViewset)

recipe_routers = routers.NestedSimpleRouter(router, 'recipes', lookup='recipe',
                                            trailing_slash=False)
recipe_routers.register(r'steps', recipe_views.StepViewset,
                        base_name='recipe-steps')
recipe_routers.register(r'ingredients', recipe_views.IngredientViewset,
                        base_name='recipe-ingredients')

auth_urls = [
    url(r'^auth$', jwt_views.obtain_jwt_token, name='auth'),
    url(r'^auth/refresh$', jwt_views.refresh_jwt_token, name='auth-refresh'),
    url(r'^auth/verify$', jwt_views.verify_jwt_token, name='auth-verify'),
]

urlpatterns = router.urls + recipe_routers.urls + auth_urls
