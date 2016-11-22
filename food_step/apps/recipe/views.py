from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Recipe, Step, Ingredient
from .serializers import RecipeSerializer, StepSerializer, IngredientSerializer
from .permissions import ChildRecipePermission, RecipePermission


class RecipeViewset(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.select_related('user')
    permission_classes = (RecipePermission,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @list_route(methods=['get', 'post'], permission_classes=[IsAuthenticated])
    def favorites(self, request, *args, **kwargs):
        qs = self.queryset.filter(user=request.user)
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        if self.request.GET.get('popular'):
            return self.queryset.order_by('favorites')
        return super(RecipeViewset, self).get_queryset()


class StepViewset(viewsets.ModelViewSet):
    serializer_class = StepSerializer
    permission_classes = (ChildRecipePermission,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_queryset(self):
        return Step.objects.filter(recipe_id=self.kwargs.get('recipe_pk'))

    def perform_create(self, serializer):
        serializer.save(recipe_id=self.kwargs.get('recipe_pk'))


class IngredientViewset(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    permission_classes = (ChildRecipePermission,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_queryset(self):
        return Ingredient.objects.filter(
            recipe_id=self.kwargs.get('recipe_pk'))

    def perform_create(self, serializer):
        serializer.save(recipe_id=self.kwargs.get('recipe_pk'))
