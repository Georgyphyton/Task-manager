from django.urls import path
from tasks import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='tasks'),
    path('create/', views.CreateTaskView.as_view(), name='create_task'),
    path('<int:pk>/update/', views.TaskEditView.as_view(),
         name='update_task'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(),
         name='delete_task'),
    path('<int:pk>', views.TaskView.as_view(),
         name='task'),
]
