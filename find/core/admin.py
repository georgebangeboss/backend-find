from django.contrib import admin
from .models import Card

# Register your models here.

class CardAdmin(admin.ModelAdmin):
    search_fields = ('id_string',)


admin.site.register(Card,CardAdmin)
