from django.db import models
from django.contrib.auth.models import User

class Solicitudes(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pendiente'),
        ('in_progress', 'En revisión'),
        ('completed', 'Completada'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
