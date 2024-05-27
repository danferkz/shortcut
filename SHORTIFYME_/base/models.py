from django.db import models

class bases(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)
    description = models.CharField(max_length=255)
    url_l = models.CharField(max_length=255)
    url_s = models.CharField(max_length=255)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.id_url