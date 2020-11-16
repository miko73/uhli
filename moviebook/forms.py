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

from django import forms
from .models import Film, Uzivatel, Tag, Zanr, Clen, Prichozi_platby, Naplanovane_platby

class FilmForm(forms.ModelForm):
    tagy = forms.ModelMultipleChoiceField(queryset = Tag.objects.all(), required = False)
	
    class Meta:
        model = Film
        fields=["nazev", "rezie", "zanr", "tagy"]
		
class ZanrForm(forms.ModelForm):
	
    class Meta:
        model = Zanr
        fields=["nazev_zanru"]
        
        
class UzivatelForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = Uzivatel
        fields = ["email", "password"]


class ClenForm(forms.ModelForm):
    class Meta:
        model = Clen
        fields = [ "email", "rc", "jmeno", "prijmeni", "narozen", "clenem_od" ]


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
