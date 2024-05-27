from django.db import models
from base.models import bases
"""""""""
class urlsmanager(bases):
    def _create_url(self, description, url_l, url_s):
        urls = self.model(
            description=description,
            url_l=url_l,
            url_s=url_s
        )
        urls.save(using=self._db)
        return urls
    
    def create_url_long(self, description, url_l):
        return self._create_url(description, url_l, None)
    
    def create_url_short(self, description, url_s):
        return self._create_url(description, None, url_s)
"""

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
