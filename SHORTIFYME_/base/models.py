from django.db import models
from user.models import CustomUser

class bases(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)
    description = models.CharField(max_length=255)
    url_l = models.URLField(verbose_name='URL original')
    url_s = models.CharField(max_length=255, verbose_name='URL corta')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Usuario', null=True, blank=True)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.id_url