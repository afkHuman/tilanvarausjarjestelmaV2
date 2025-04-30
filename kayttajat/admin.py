from django.contrib import admin
from .models import Kayttaja

# Register your models here.

class KayttajaAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Kayttaja, KayttajaAdmin)