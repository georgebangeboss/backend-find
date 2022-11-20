from .models import Card
from .serializers import CardSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class CardCreateAPIView(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardUpdateAPIView(generics.UpdateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDeleteAPIView(generics.DestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardListAPIView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (
        SearchFilter,
        OrderingFilter,
        DjangoFilterBackend,
    )
    filterset_fields = [
        "college_name",
        "department",
        "location_found",
        "status",
    ]
    search_fields = (
        "name",
        "reg_number",
        "id_string",
    )
