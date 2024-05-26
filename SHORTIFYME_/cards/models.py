from django.db import models
from url.models import url

class cards (model.Model):
    id_url_main = models.ForeignKey('url', on_delete=models.url, verbose_name='url', null=True, blank=True)
    id_url_short = models.ForeignKey('url_short', on_delete=models.url, verbose_name='url_short', null=True, blank=True)
# Create your models here.
