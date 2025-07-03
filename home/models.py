from django.db import models
import datetime

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDesc = models.TextField()
    time = models.DateTimeField(auto_now_add=True, editable = True)
    
    def __str__(self):
        return self.taskTitle