from goods.models import Product, Category
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'discount', 'quantity', 'rate']
