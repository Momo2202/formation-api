from django.db import models


class Formateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True)
    specialite = models.CharField(max_length=150)
    actif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nom", "prenom"]
        verbose_name = "formateur"
        verbose_name_plural = "formateurs"

    def __str__(self):
        return f"{self.prenom} {self.nom}"
