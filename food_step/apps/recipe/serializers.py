from rest_framework import serializers

from apps.core.serializers import UserSerilizer
from .models import Recipe, Step, Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    user = UserSerilizer()
    favorites = serializers.HyperlinkedIdentityField(
        view_name='api:user-detail', read_only=True, many=True)
    favorited = serializers.SerializerMethodField()

    def get_favorited(self, obj):
        return obj.is_favorited(self.context.get('request').user)

    class Meta:
        model = Recipe
        fields = '__all__'
        kwargs = {
            'favorites': {'required': False}
        }


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
