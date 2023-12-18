from todo.models import Task
from todo.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

'''
creating views using ModelViewSet
'''
class TaskModelViewSet(ModelViewSet):
    permission_classes= [IsAuthenticatedOrReadOnly]
    queryset = Task.objects.filter()
    serializer_class = TaskSerializer
    
