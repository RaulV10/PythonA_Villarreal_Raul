from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserRequestListView.as_view(), name='user_request_list'),
    path('create_request/', views.create_request, name='create_request'),
    path('edit_request/<int:request_id>/', views.edit_request, name='edit_request'),
    path('delete_request/<int:request_id>/', views.delete_request, name='delete_request'),
    path('change_status/<int:request_id>/', views.change_status, name='change_status'),
]