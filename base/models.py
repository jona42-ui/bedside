from django.db import models

# Create your models here.

class Message(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    message = models.CharField(max_length=1000)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return f'{self.email} - {self.first_name}'
