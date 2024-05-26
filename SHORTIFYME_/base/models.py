from django.db import models

# Create your models here.
class bases (models.Model):     
    id_url = models.CharField(max_length=255)
    dir_url = models.CharField(max_length=350)
    page_url= models.CharField(max_length=255)

    def __str__(self):
        return self.id_url