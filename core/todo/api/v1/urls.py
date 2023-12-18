from django.urls import path
from .views import TaskModelViewSet
from rest_framework.routers import DefaultRouter

app_name='api-v1'

router = DefaultRouter()
router.register('task', TaskModelViewSet,basename='task')
urlpatterns = router.urls