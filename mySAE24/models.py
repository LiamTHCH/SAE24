from django.db import models

class Capteur(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    nom = models.CharField(max_length=100)
    piece = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.id}"
        return chaine

    def dico(self):
        return {"nom": self.nom,"piece": self.piece, "emplacement": self.emplacement}


class Data(models.Model):
    temp = models.CharField(max_length=200)
    timestamp = models.DateTimeField(max_length=200)
    capteur = models.ForeignKey(Capteur, on_delete=models.CASCADE,blank=False)

    def __str__(self):
        chaine = self.temp + "°C " + self.capteur.id
        return chaine

    def dico(self):
        return {"data": self.data,"timestamp": self.timestamp, "capteur": self.capteur}

