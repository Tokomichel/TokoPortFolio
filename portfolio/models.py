from django.db import models

# Create your models here.

class Projects(models.Model):
    nom = models.CharField(max_length = 20)
    description = models.TextField(max_length = 300)
    start_date = models.DateField
    date_debut = models.DateField(blank=False)
    date_fin = models.DateField(blank=True)
    imageP = models.ImageField(blank=False, upload_to='photo/')
    image2 = models.ImageField(blank=True,upload_to='photo/')
    image3 = models.ImageField(blank=True,upload_to='photo/')
    en_equipe = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.nom

class Techs(models.Model):
    tech_name = models.CharField(max_length = 25)
    tech_pic = models.ImageField(blank= False, upload_to = 'photo/')
    project = models.ManyToManyField(Projects)

    def __str__(self):
        return self.tech_name

