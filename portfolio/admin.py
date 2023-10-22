from django.contrib import admin
from .models import *

class Project_view(admin.ModelAdmin):
    list_display = ["id", 'nom', 'en_equipe', 'date_debut', 'date_fin']

class Techs_view(admin.ModelAdmin):
    list_display = ['id','tech_name']
# Register your models here.

admin.site.register(Projects, Project_view)
admin.site.register(Techs, Techs_view)
