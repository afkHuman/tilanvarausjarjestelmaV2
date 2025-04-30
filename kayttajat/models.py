from django.db import models

# Create your models here.

class Kayttaja(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
  
# Kokeillaan korjata Kayttajas virhe admin sivulla
  #class Meta:
  #  verbose_name= 'Kayttajat'
  #  verbose_name_plurar= 'Kayttajas'