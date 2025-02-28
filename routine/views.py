from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from routine.models import Routine
from routine.paginators import RoutinePagination
from routine.serializers import RoutineSerializer
from users.permissions import IsOwner


class RoutineViewSet(ModelViewSet):
    """Класс, описывающий ViewSet для модели Привычка"""
    pagination_class = RoutinePagination
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

    def get_serializer_context(self):
        """Получаем контекст сериализатора модели Привычка и добавляем к нему поле request"""
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_permissions(self):
        """Определяем permissions согласно предоставляемым пользователю правам"""
        if self.action in ["update", "retrieve", "partial_update", "destroy", "create"]:
            self.permission_classes = (IsOwner,)
        elif self.action in ["list"]:
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()


class RoutineCreateAPIView(CreateAPIView):
    """Класс, описывающий APIView для создания экземпляра модели Привычка"""
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Метод для создания экземпляра модели Привычка с привязкой к текущему пользователю"""
        routine = serializer.save()
        routine.owner = self.request.user
        routine.save()


class RoutineListAPIView(ListAPIView):
    """Класс, описывающий APIView для вывода списка Привычек текущего пользователя"""
    pagination_class = RoutinePagination
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = (IsOwner,)

    def get(self, request, *args, **kwargs):
        """Метод обработки запроса GET, фильтрующий привычки по текущему пользователю"""
        queryset = Routine.objects.filter(owner=self.request.user)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = RoutineSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class RoutinePublicListAPIView(ListAPIView):
    """Класс, описывающий APIView для вывода списка публичных Привычек: поле is_public=True"""
    pagination_class = RoutinePagination
    queryset = Routine.objects.filter(is_public=True)
    serializer_class = RoutineSerializer
    permission_classes = (IsAuthenticated,)
