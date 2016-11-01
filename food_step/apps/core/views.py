from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from apps.recipe.models import Recipe
from apps.recipe.serializers import RecipeSerializer
from .serializers import UserSerilizer


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerilizer
    queryset = User.objects.all()

    @detail_route()
    def recipes(self, request, *args, **kwargs):
        recipes = Recipe.objects.select_related('user')\
            .filter(user_id=self.kwargs.get('pk'))
        serializer = RecipeSerializer(
            recipes, many=True, context={'request': request})
        return Response(serializer.data)
