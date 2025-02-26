from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from routine.models import Routine
from routine.paginators import RoutinePagination
from routine.serializers import RoutineSerializer
from users.permissions import IsOwner


class RoutineViewSet(ModelViewSet):
    pagination_class = RoutinePagination
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_permissions(self):
        if self.action in ["update", "retrieve", "partial_update", "destroy", "create"]:
            self.permission_classes = (IsOwner,)
        elif self.action in ["list"]:
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()


class RoutineCreateAPIView(CreateAPIView):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        routine = serializer.save()
        routine.owner = self.request.user
        routine.save()


class RoutineListAPIView(ListAPIView):
    pagination_class = RoutinePagination
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = (IsOwner,)

    def get(self, request, *args, **kwargs):
        queryset = Routine.objects.filter(owner=self.request.user)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = RoutineSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class RoutinePublicListAPIView(ListAPIView):
    pagination_class = RoutinePagination
    queryset = Routine.objects.filter(is_public=True)
    serializer_class = RoutineSerializer
    permission_classes = (IsAuthenticated,)
