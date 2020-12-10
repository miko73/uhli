from django.test import TestCase

from datetime import date
from moviebook.models import Akce, Film, Zanr, Tag, Uzivatel, UzivatelManager
from moviebook.models import Film, Zanr, Clen, Akce, Ucastnici
clen = Clen() # Vytvoríme si nový film
clen = Clen.objects.get(id = 1)
print("Clen : " + clen.prijmeni)
conn.close()