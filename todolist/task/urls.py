from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('task_list', views.task_lists, name = 'task'),
    path('create_task', views.create_task, name = 'create'),
    path('delete_task/<int:task_id>', views.delete_task, name = 'delete'),
    path('update_task/<int:task_id>', views.update_task, name = 'update'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout_view, name = 'logout'),
    path('password_reset', views.password_reset, name = 'password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('password_reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('password_reset/done', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
    
]