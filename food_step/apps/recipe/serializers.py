from rest_framework import serializers

from apps.core.serializers import UserSerilizer
from .models import Recipe, Step, Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    user = UserSerilizer()
    favorites = serializers.SerializerMethodField()
    favorited = serializers.SerializerMethodField()

    def get_favorited(self, obj):
        return obj.is_favorited(self.context.get('request').user)

    def get_favorites(self, obj):
        return obj.favorites.count()

    class Meta:
        model = Recipe
        fields = '__all__'
        kwargs = {
            'favorites': {'required': False},
            'user': {'reqired': False}
        }


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
