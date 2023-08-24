from django.urls import path
from users import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='users'),
    path('create/', views.RegisterView.as_view(), name='create_user'),
    path('<int:pk>/update/', views.UserEditView.as_view(),
         name='update_user'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(),
         name='delete_user'),
]
