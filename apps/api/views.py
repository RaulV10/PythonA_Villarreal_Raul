from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from apps.api.models import Solicitudes
from apps.api.serializers import SolicitudesSerializer

class TokenObtainView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Se requiere nombre de usuario y contraseña.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                if user.groups.filter(name__in=["api", "administrador"]).exists():
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'access_token': str(refresh.access_token),
                        'refresh_token': str(refresh),
                    })
                else:
                    return Response({'error': 'Este usuario no tiene los permisos para acceder a la API'}, status=status.HTTP_401_UNAUTHORIZED)

        except User.DoesNotExist:
            pass

        return Response({'error': 'Credenciales inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)

class SolicitudesListaView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Solicitudes.objects.all()
    serializer_class = SolicitudesSerializer

class SolicitudesDetalleView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Solicitudes.objects.all()
    serializer_class = SolicitudesSerializer

class SolicitudesListaCustomView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        solicitudes = Solicitudes.objects.filter(activo=True)
        serializer = SolicitudesSerializer(solicitudes, many=True)
        return Response(serializer.data)

    def post(self, request):
        solicitud = Solicitudes(
            title=request.data['title'],
            description=request.data['description'],
            location=request.data['location'],
            status=request.data['status'],
            user=request.user
        )
        solicitud.save()
        serializer = SolicitudesSerializer(solicitud)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SolicitudesDetalleCustomView(APIView):
    def get_permissions(self):
        methods_protected = ['PUT', 'PATCH', 'DELETE']
        if self.request.method in methods_protected:
            return [IsAuthenticated()]
        return []

    def get_object(self, pk):
        try:
            return Solicitudes.objects.get(pk=pk)
        except Solicitudes.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        solicitud = self.get_object(pk)
        serializer = SolicitudesSerializer(solicitud)
        return Response(serializer.data)

    def put(self, request, pk):
        solicitud = self.get_object(pk)
        serializer = SolicitudesSerializer(solicitud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        solicitud = self.get_object(pk)
        serializer = SolicitudesSerializer(solicitud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        solicitud = self.get_object(pk)
        solicitud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
