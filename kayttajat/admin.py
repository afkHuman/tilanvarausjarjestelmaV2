from django.contrib import admin
from .models import UusiKayttaja, UusiTila

# Register your models here.

# Järjestelmänvalvojan rakenne MemberAdmin luokalle, joka hyödyntää UusiKayttaja-mallia
class MemberAdmin(admin.ModelAdmin):
  # TODO: Kysy Markulta
  """Admin interface for managing user instances.

  Args:
      admin (ModelAdmin): The base admin class.
  """
  list_display = ("firstname", "lastname", "joined_date",)
  prepopulated_fields = {"slug": ("firstname", "lastname")}

admin.site.register(UusiKayttaja, MemberAdmin)


# Järjestelmänvalvojan rakenne SpaceAdmin luokalle, joka hyödyntää UusiTila-mallia
class SpaceAdmin(admin.ModelAdmin):
  # TODO: Kysy Markulta
  """Admin interface for managing space instances.

  Args:
      admin (ModelAdmin): The base admin class.
  """
  list_display = ("idNumber", "location", "privatespace", "publicspace", "purpose", "size", "capacity", "rental", "loan", "reservation",)
  prepopulated_fields = {"slug": ("purpose", "location")}

admin.site.register(UusiTila, SpaceAdmin)
