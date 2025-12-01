from django.db import models

# Create your models here.

class Feedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    


