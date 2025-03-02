from django.urls import path
from rest_framework.routers import SimpleRouter

from routine.apps import RoutineConfig
from routine.views import RoutineViewSet, RoutinePublicListAPIView, RoutineListAPIView, RoutineCreateAPIView

app_name = RoutineConfig.name

router = SimpleRouter()
router.register('', RoutineViewSet)

urlpatterns = [
    path('public/', RoutinePublicListAPIView.as_view(), name='public'),
    path('', RoutineListAPIView.as_view(), name='routine-list'),
    path('create/', RoutineCreateAPIView.as_view(), name='routine-create'),
]

urlpatterns += router.urls
