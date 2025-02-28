from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Класс, описывающий сериализатор для модели Пользователь"""
    class Meta:
        model = User
        fields = "__all__"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Класс, описывающий сериализатор для получения токена для авторизации Пользователя"""
    @classmethod
    def get_token(cls, user):
        """Метод получения токена для авторизации Пользователя"""
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['password'] = user.password
        token['email'] = user.email

        return token
