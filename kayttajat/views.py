from django.http import HttpResponse
from django.template import loader
from .models import User,Space
from django.shortcuts import get_object_or_404

# Käytetty esimerkissä
# from django.db.models import Q
# https://www.w3schools.com/django/django_queryset_filter.php/ Filtterointi tapoja/suodatustapoja koodiin!

# Pääsivu näkymä applikaatioille
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

# Käyttäjät näkymä applikaatiolle
def kayttajat(request):
  mymembers = User.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  
  return HttpResponse(template.render(context, request))

# Käyttäjän yksityiskohtien näkymä applikaatiolle
def users_details(request, slug):
  mymember = User.objects.get(slug=slug)
  template = loader.get_template('users_details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

# Tilat näkymä applikaatioille
def tilat(request):
  myspaces = Space.objects.all().values()
  template = loader.get_template('all_spaces.html')
  context = {
    'myspaces': myspaces,
  }
  
  return HttpResponse(template.render(context, request))

# Tilojen yksityiskohtien näkymä applikaatioille
def spaces_details(request, slug):
    myspaces = get_object_or_404(Space, slug=slug)
    template = loader.get_template('spaces_details.html')
    context = {
        'myspaces': myspaces,
    }
    return HttpResponse(template.render(context, request))
