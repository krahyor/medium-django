from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.permissions import IsAuthenticated


from medium.common.utils import CustomRenderer
from medium.api.serializers.accounts import (
    ChangePasswordSerializer,
    RegisterSerializer,
    LoginSerializer,
    RefreshTokenSerializer,
)


class AccountLoginView(TokenViewBase):
    serializer_class = LoginSerializer
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class AccountRegisterView(generics.CreateAPIView):
    permission_classes = ()
    serializer_class = RegisterSerializer
    renderer_classes = [BrowsableAPIRenderer, CustomRenderer]


class AccountRefreshTokenView(TokenViewBase):
    serializer_class = RefreshTokenSerializer
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class AccountChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)

        if not serializer.is_valid():
            raise APIException(serializer.errors)

        user = request.user
        password = serializer.validated_data.get("password")
        new_password = serializer.validated_data.get("new_password")

        if not user.check_password(password):
            raise APIException("invalid_password")

        user.set_password(new_password)
        user.save()

        return Response("success")
