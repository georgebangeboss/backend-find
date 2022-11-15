from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("create", views.CardCreateAPIView.as_view()),
    path("retrieve/<pk>/", views.CardRetrieveAPIView.as_view()),
    path("update/<pk>/", views.CardUpdateAPIView.as_view()),
    path("delete/<pk>/", views.CardDeleteAPIView.as_view()),
    path("list/", views.CardListAPIView.as_view()),
    re_path("^search/(?P<searchword>[\w]+)/$", views.CardFilterAPIView.as_view()),
]
