import django_filters

from .models import Formateur


class FormateurFilter(django_filters.FilterSet):
    specialite = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Formateur
        fields = ["actif", "specialite"]
