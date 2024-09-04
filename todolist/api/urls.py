from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskListView, UpdateTaskView, DeleteTaskView, UsersList
from task.models import Task
from .serializers import TaskSerializer

router = DefaultRouter()
router.register('tasklist', TaskListView, basename='tasklist')


urlpatterns = [
    # path('', include(router.urls)),
    path('', TaskListView.as_view (queryset = Task.objects.all(), serializer_class = TaskSerializer)),
    path('update_task_api/<int:pk>', UpdateTaskView.as_view(), name= 'updateAPI'),
    path('delete_task_api/<int:pk>', DeleteTaskView.as_view(), name= 'deleteAPI'),
    path('return_users_api/', UsersList.as_view(), name= 'returnUser'),

]