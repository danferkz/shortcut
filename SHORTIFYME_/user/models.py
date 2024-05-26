from django.db import models


# Create your models here.
class users (models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(max_length=100, verbose_name='Email')
    password = models.CharField(max_length=100, verbose_name='Password')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
