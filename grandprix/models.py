from django.db import models

class Pilote(models.Model):
    id_technique = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=100)
    equipe = models.CharField(max_length=100)
    titres = models.IntegerField(default=0)
    podiums = models.IntegerField(default=0)
    victoires = models.IntegerField(default=0)
    bio = models.TextField(blank=True)
    img_url = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return self.nom