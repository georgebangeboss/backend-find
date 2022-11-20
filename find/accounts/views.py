from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.serializers import RegistrationSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
@api_view(["POST"])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["id"] = account.pk
            data["email"] = account.email
            token = Token.objects.get(user=account).key
            data["token"] = token
        else:
            data = serializer.errors
        return Response(data)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def view_profile_view(request):
    try:
        user = request.user
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


@api_view(["PUT"])
# @permission_classes((IsAuthenticated,))
def update_profile_view(request):
    try:
        user = request.user
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = UserProfileSerializer(user, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["response"] = "successful update"
            return Response(data=data)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(LoginView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response({"token": token.key, "id": token.user_id})
