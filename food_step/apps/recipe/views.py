from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route

from .models import Recipe, Step, Ingredient
from .serializers import RecipeSerializer, StepSerializer, IngredientSerializer


class RecipeViewset(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    @list_route()
    def favorites(self, request, *args, **kwargs):
        qs = self.queryset.filter(user=request.user)
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)


class StepViewset(viewsets.ModelViewSet):
    serializer_class = StepSerializer

    def get_queryset(self):
        return Step.objects.filter(recipe_id=self.kwargs.get('recipe_pk'))


class IngredientViewset(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        return Ingredient.objects.filter(
            recipe_id=self.kwargs.get('recipe_pk'))
