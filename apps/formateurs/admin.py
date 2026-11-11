from django.contrib import admin

# Register your models here.
from .models import Formateur


@admin.register(Formateur)
class FormateurAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "email", "specialite", "actif")
    list_filter = ("actif", "specialite")
    search_fields = ("nom", "prenom", "email")
    ordering = ("nom", "prenom")
