from django.db import models

# Create your models here.

# Malli joka kuvaa Uuutta käyttäjää sovelluksessa.
class UusiKayttaja(models.Model):
  """Model representing a user in the application.

  Args:
      firstname (str): First name of the user
      lastname (str): Last name of the user
      phone (int): Phone number of the user
      joined_date (date): Date when the user joined
      slug (str): Slug field for URL identification

  Returns:
      str: String representation of the user
  """
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  slug = models.SlugField(default="", null=False)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

# Malli joka kuvaa uutta tilaa sovelluksessa.
class UusiTila(models.Model):
  """Model representing new space in the application.

  Args:
      idNumber (int): Unique identifier for the space
      privatespace (bool): Indicates if the space is private
      publicspace (bool): Indicates if the space is public
      location (str): Location of the space
      purpose (str): Purpose of the space
      size (float): Size of the space in square meters
      capacity (int): Capacity of the space
      rental (bool): Indicates if the space is available for rental
      loan (bool): Indicates if the space can be loaned
      reservation (bool): Indicates if the space can be reserved
      slug (str): Slug field for URL identification

  Returns:
      str: String representation of the space
  """
  idNumber = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
  location = models.CharField(max_length=255, null=False)
  privatespace = models.BooleanField(default=False)
  publicspace = models.BooleanField(default=False)
  purpose = models.CharField(max_length=255, null=False)
  size = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Size m²", default=0.0, blank=True)
  capacity = models.IntegerField(default=0, blank=True)
  rental = models.BooleanField(default=False)
  loan = models.BooleanField(default=False)
  reservation = models.BooleanField(default=False)
  slug = models.SlugField(default="", null=False)

  def __str__(self):
    # Jos haluat nähdä kaikki kentät merkkijonona, voit käyttää alla olevaa riviä:
    #return f"ID: {self.idNumber} | Location: {self.location} | Private: {self.privatespace} | Public: {self.publicspace} | Purpose: {self.purpose} | Size: {self.size} m² | Capacity: {self.capacity} | Rental: {self.rental} | Loan: {self.loan} | Reservation: {self.reservation}"
    
    # Tai jos haluat vain ID:n, voit käyttää alla olevaa riviä:
    return f"ID: {self.idNumber}"