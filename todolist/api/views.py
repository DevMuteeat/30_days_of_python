from django.shortcuts import render
from rest_framework import viewsets, permissions
from task.models import Task, User
from .serializers import TaskSerializer, UserSerializer
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from django.db.models import Q

# Create your views here.

class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class UpdateTaskView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field  = 'pk'

    def get(self, request, *args, **kwargs):
        task = self.get_object()

        serializer = self.serializer_class(task)

        return Response(serializer.data)
    
class DeleteTaskView(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field  = 'pk'

class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    # lookup_field = 'pk'
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return Task.objects.all()
    #     return User.objects.filter(Q(created_by=user) | Q(assigned_to=user))