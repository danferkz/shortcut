from django.db import models
from base.models import bases


class tag(models.Model):
    tagName = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
    
    def __str__(self):
        return self.tagName
    

class cards(bases):
    id_card = models.AutoField(primary_key=True)
    tagName = models.ForeignKey(tag, on_delete=models.CASCADE, verbose_name='tag', null=True, blank=True)
    class Meta:
        verbose_name = 'card'
        verbose_name_plural = 'cards'
    
    def __str__(self):
        return str(self.id_card)
