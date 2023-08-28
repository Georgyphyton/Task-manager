from django.urls import path
from labels import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='labels'),
    path('create/', views.CreateLabelView.as_view(), name='create_label'),
    path('<int:pk>/update/', views.LabelEditView.as_view(),
         name='update_label'),
    path('<int:pk>/delete/', views.LabelDeleteView.as_view(),
         name='delete_label'),
]
