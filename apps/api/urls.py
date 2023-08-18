from django.urls import path
from . import views

urlpatterns = [
    path('token/', views.TokenObtainView.as_view(), name='token_obtain'),
    path('solicitudes/', views.SolicitudesListaView.as_view(), name='solicitud-list'),
    path('solicitudes/<int:pk>/', views.SolicitudesDetalleView.as_view(), name='solicitud-detail'),
    path('solicitudes/custom/', views.SolicitudesListaCustomView.as_view(), name='solicitud-list-custom'),
    path('solicitudes/custom/<int:pk>/', views.SolicitudesDetalleCustomView.as_view(), name='solicitud-detail-custom'),
]
