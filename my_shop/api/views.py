
from rest_framework import permissions, generics

from goods.models import Product
from .serializers import ProductSerializer


class ProductViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
