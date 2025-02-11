from rest_framework import viewsets
from django.db.models import Prefetch
from .models import FoodCategory, Food
from .serializers import FoodListSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.filter(
            food__is_publish=True
        ).distinct().order_by('id').prefetch_related(
            Prefetch('food', queryset=Food.objects.filter(is_publish=True))
        )
    serializer_class = FoodListSerializer
