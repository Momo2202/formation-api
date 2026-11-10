import pytest
from django.db import connection


@pytest.mark.django_db
def test_connexion_base_de_donnees():
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        assert cursor.fetchone() == (1,)
