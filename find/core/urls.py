from django.urls import path
from . import views


urlpatterns = [
    path("create", views.CardCreateAPIView.as_view()),
    path("retrieve/<pk>/", views.CardRetrieveAPIView.as_view()),
    path("update/<pk>/", views.CardUpdateAPIView.as_view()),
    path("delete/<pk>/", views.CardDeleteAPIView.as_view()),
    path("list/", views.CardListAPIView.as_view(), name="list"),
]
