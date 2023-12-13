from rest_framework.serializers import ModelSerializer
from food_app.models import Food


class FoodSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Food


class FoodDetailSerializer(ModelSerializer):
 
    class Meta:
        fields = ("id", "name", "publisher_name", "featured_image", "ingredients", "description")
        model = Food


