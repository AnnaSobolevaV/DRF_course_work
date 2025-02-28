from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserSerializer, MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    """Класс, описывающий View для получения токена для авторизации Пользователя"""
    serializer_class = MyTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Класс, описывающий ViewSet для модели Пользователь"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(CreateAPIView):
    """Класс, описывающий APIView для создания экземпляра модели Пользователь"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Метод создания экземпляра модели Пользователь, активация пользователя и хеширование пароля"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PasswordResetAPIView(UpdateAPIView):
    """Класс, описывающий APIView для сброса пароля Пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        """Метод изменения пароля Пользователя"""
        user = serializer.save()
        user.set_password(user.password)
        user.save()
