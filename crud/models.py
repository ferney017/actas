from django.db import models

# Modelo Crud
class Crud(models.Model):
    title = models.CharField(max_length=200)  # Campo de texto corto
    description = models.TextField()          # Texto largo
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación

    def __str__(self):
        return self.title
