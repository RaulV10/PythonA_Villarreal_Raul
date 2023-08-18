from django.contrib.auth.models import User
from django.test import TestCase, Client
from rest_framework import status
from apps.api.models import Solicitudes
from apps.api.serializers import SolicitudesSerializer

class RequestTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_request(self):
        data = {'title': 'Test Title', 'description': 'Test Description', 'location': 'Test Location', 'status': 'pending', 'user': '1'}
        response = self.client.post('/solicitudes/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Debes verificar el código correcto aquí

    def test_edit_request(self):
        # Crear un usuario de prueba
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Crear una solicitud asociada al usuario
        request = Solicitudes.objects.create(title='Original Title', description='Original Description', location='Original Location', status='pending', user=user)

        # Datos para editar la solicitud
        data = {'title': 'Updated Title', 'description': 'Updated Description'}
        response = self.client.put(f'/solicitudes/{request.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_request = Solicitudes.objects.get(id=request.id)
        self.assertEqual(updated_request.title, 'Updated Title')
        self.assertEqual(updated_request.description, 'Updated Description')
