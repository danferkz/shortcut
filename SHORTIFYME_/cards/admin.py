from django.contrib import admin

# Register your models here.
from .models import cards
from .models import tag

admin.site.register(cards)
admin.site.register(tag)