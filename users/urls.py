from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import UserViewSet, MyTokenObtainPairView, UserCreateAPIView, PasswordResetAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('password_reset/<int:pk>/', PasswordResetAPIView.as_view(), name='password_reset'),
    path('login/', MyTokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]

urlpatterns += router.urls
