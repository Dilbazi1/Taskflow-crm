from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from ..models import Task
from .serializers import TaskSerializer
from ..permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from users.permissions import IsOperatorOrAdmin, IsAdmin

class TaskViewSet(ModelViewSet):
        serializer_class = TaskSerializer
        queryset = Task.objects.all()

        def get_queryset(self):
            user = self.request.user
            return Task.objects.filter(
                Q(created_by=user) | Q(assigned_to=user)
            ).distinct()

        def perform_create(self, serializer):
            serializer.save(created_by=self.request.user)

        def get_permissions(self):
            if self.action == 'destroy':
                return [IsAdmin()]
            if self.action in ['create', 'update', 'partial_update']:
                return [IsOperatorOrAdmin()]
            return [IsAuthenticated()]