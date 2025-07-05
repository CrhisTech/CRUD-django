from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField() #Fecha y hora para realizar la tarea
    created_at = models.DateTimeField(auto_now_add=True) #Fecha y hora actual
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['date'] # Ordenar por fecha de realizacion
        
