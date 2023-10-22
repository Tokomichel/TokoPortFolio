from django.shortcuts import *
from .models import *
from .deuko import *
# Create your views here.

def FirstView(requete):
    project = Projects.objects.all()
    techs = Techs.objects.all()
    list_projet = []

    for elt in project:
      pro = Proj(nom = elt.nom,
       description = elt.description,
        url = elt.imageP.url,
        occ = len(project))
     # pro.techs(list(elt.techs_set.all()))
      for i in elt.techs_set.all():
        # print(i, elt.nom)
        pro.liste_tech.append(i)

      list_projet.append(pro)
    
    project = Projects.objects.all()
    techs = Techs.objects.all()

    techs[3].project.add(project[0])   
    return render(requete, 'index.html', {"pro": list_projet, 'techs':techs})

def ajout_tech(requete):  
    project = Projects.objects.all()
    techs = Techs.objects.all()

    for elt in techs:
        elt.project.add(project[3])
    return HttpResponse("<h1 align='center'>C'est fait</h1>")


