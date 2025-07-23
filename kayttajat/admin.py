from django.contrib import admin
from .models import UusiKayttaja, UusiTila

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  prepopulated_fields = {"slug": ("firstname", "lastname")}

admin.site.register(UusiKayttaja, MemberAdmin)

class SpaceAdmin(admin.ModelAdmin):
  list_display = ("size", "capacity", "purpose", "location", "rental", "loan", "reservation",)
  prepopulated_fields = {"slug": ("size", "location")}

admin.site.register(UusiTila, SpaceAdmin)
