from django.http import HttpResponse
from django.template import loader
from .models import UusiKayttaja,UusiTila

# Käytetty esimerkissä
# from django.db.models import Q
# https://www.w3schools.com/django/django_queryset_filter.php/ Filtterointi tapoja/suodatustapoja koodiin!

def kayttajat(request):
  mymembers = UusiKayttaja.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  
  return HttpResponse(template.render(context, request))

def tilat(request):
  myspaces = UusiTila.objects.all().values()
  template = loader.get_template('all_spaces.html')
  context = {
    'myspaces': myspaces,
  }
  
  return HttpResponse(template.render(context, request))

def details(request, slug):
  mymember = UusiKayttaja.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
