# Create your views here.
from rest_framework import viewsets

from .filters import FormateurFilter
from .models import Formateur
from .serializers import FormateurSerializer


class FormateurViewSet(viewsets.ModelViewSet):
    queryset = Formateur.objects.all()
    serializer_class = FormateurSerializer
    filterset_class = FormateurFilter
    search_fields = ["nom", "prenom", "email", "specialite"]
    ordering_fields = ["nom", "prenom", "created_at"]
