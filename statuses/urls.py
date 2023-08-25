from django.urls import path
from statuses import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='statuses'),
    path('create/', views.CreateStatusView.as_view(), name='create_status'),
    path('<int:pk>/update/', views.StatusEditView.as_view(),
         name='update_status'),
    path('<int:pk>/delete/', views.StatusDeleteView.as_view(),
         name='delete_status'),
]
