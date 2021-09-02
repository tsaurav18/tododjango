from django.db import models
from django.utils import timezone
# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(blank=True, default='do it')
    created=models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    due_date=models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.title