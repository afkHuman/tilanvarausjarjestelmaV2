from django.contrib import admin
from .models import UusiKayttaja, UusiTila

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  prepopulated_fields = {"slug": ("firstname", "lastname")}

admin.site.register(UusiKayttaja, MemberAdmin)

class SpaceAdmin(admin.ModelAdmin):
  list_display = ("idNumber", "location", "purpose", "size", "capacity", "rental", "loan", "reservation",)
  prepopulated_fields = {"slug": ("purpose", "location")}

admin.site.register(UusiTila, SpaceAdmin)
