#  _____ _______         _                      _
# |_   _|__   __|       | |                    | |
#   | |    | |_ __   ___| |___      _____  _ __| | __  ___ ____
#   | |    | | '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ / / __|_  /
#  _| |_   | | | | |  __/ |_ \ V  V / (_) | |  |   < | (__ / /
# |_____|  |_|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_(_)___/___|
#                                _
#              ___ ___ ___ _____|_|_ _ _____
#             | . |  _| -_|     | | | |     |  LICENCE
#             |  _|_| |___|_|_|_|_|___|_|_|_|
#             |_|
#
# IT ZPRAVODAJSTVÍ  <>  PROGRAMOVÁNÍ  <>  HW A SW  <>  KOMUNITA
#
# Tento zdrojový kód je součástí výukových seriálů na
# IT sociální síti WWW.ITNETWORK.CZ
#
# Kód spadá pod licenci prémiového obsahu a vznikl díky podpoře
# našich členů. Je určen pouze pro osobní užití a nesmí být šířen.
# Více informací na http://www.itnetwork.cz/licence

from django.test import TestCase

from datetime import date
from moviebook.models import Akce, Film, Zanr, Tag, Uzivatel, UzivatelManager
from moviebook.models import Film, Zanr, Clen, Akce, Ucastnici
clen = Clen() # Vytvoríme si nový film
clen = Clen.objects.get(id = 1)
print("Clen : " + clen.prijmeni)
conn.close()