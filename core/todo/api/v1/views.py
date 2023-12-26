from todo.models import Task
from todo.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsOwnerOrReadOnly
from .paginations import DefaultPagination



'''
creating views using ModelViewSet
'''
class TaskModelViewSet(ModelViewSet):
    permission_classes= [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    pagination_class = DefaultPagination
    queryset = Task.objects.filter()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['complete']
    search_fields = ['title']
    ordering_fields = ['created_date']
    
