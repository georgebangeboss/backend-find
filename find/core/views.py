from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings
from .models import Card
from .serializers import CardSerializer
from rest_framework import generics


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


class CardFilterAPIView(generics.ListAPIView):
    serializer_class = CardSerializer
    lookup_url_kwarg = "searchword"

    def get_queryset(self):
        searchWord = self.kwargs.get(self.lookup_url_kwarg)
        print(searchWord)
        return Card.objects.filter(
            first_name__icontains=searchWord,
        )
