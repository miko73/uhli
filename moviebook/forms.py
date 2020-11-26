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
        fields = [ "jmeno", "prijmeni", "narozen", "email", "rc", "clenem_od", "active", "prijmeni_rodic", "facr_id", "var_symbol", "klub_id", "cislo_uctu", "telefonni_cislo", "typ_clena", 
        "ucet_protiucet", "ucet_protiucet2", "ucet_kod_banky", "ucet_zprava_pro_prijemce", "ucet_poznamka", "ucet_nazev_protiuctu", "rok_narozeni" ]
        widgets = {
            'jmeno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Křestní jméno'}),
            'prijmeni': forms.TextInput(attrs={'class': 'form-control', }),
            'narozen': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', }),
            'rc': forms.TextInput(attrs={'class': 'form-control', }),
            'clenem_od': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-control', }),
            'prijmeni_rodic': forms.TextInput(attrs={'class': 'form-control', }),
            'facr_id': forms.TextInput(attrs={'class': 'form-control', }),
            'var_symbol': forms.TextInput(attrs={'class': 'form-control', }),
            'klub_id': forms.TextInput(attrs={'class': 'form-control', }),
            'cislo_uctu': forms.TextInput(attrs={'class': 'form-control', }),
            'telefonni_cislo': forms.TextInput(attrs={'class': 'form-control', }),
            'typ_clena': forms.TextInput(attrs={'class': 'form-control', }),
            'ucet_protiucet': forms.TextInput(attrs={'class': 'form-control', }),
            'ucet_protiucet2': forms.TextInput(attrs={'class': 'form-control', }),
            'ucet_kod_banky': forms.TextInput(attrs={'class': 'form-control', }),
            'ucet_zprava_pro_prijemce':forms.TextInput(attrs={'class': 'form-control', }),
            'ucet_poznamka': forms.TextInput(attrs={'class': 'form-control', }),
            'ucet_nazev_protiuctu': forms.TextInput(attrs={'class': 'form-control', }),
            'rok_narozeni': forms.TextInput(attrs={'class': 'form-control', }),
        }
        labels = {
            'jmeno': ('Jméno)'),
            'prijmeni': ('Příjemení'),
            'Narozen': ('narozen'),
            'email': ('Email'),
            'rc': ('Rodné číslo'),
            'clenem_od': ('Členem od'),
            'active' : ('Aktivní'),
            'prijmeni_rodic': ('Příjemení rodiče'),
            'facr_id': ('FAČR ID'),
            'var_symbol': ('Var. symbol'),
            'klub_id': ('Klub ID'),
            'cislo_uctu': ('Č. účtu'),
            'telefonni_cislo': ('Tel. číslo'),
            'typ_clena':('Typ člena'),
            'ucet_protiucet': ('Protiůčet'),
            'ucet_protiucet2': ('Protiůčet 2'),
            'ucet_kod_banky': ('Kód banky'),
            'ucet_zprava_pro_prijemce': ('Zpráva pp'),
            'ucet_poznamka': ('Poznámka'),
            'ucet_nazev_protiuctu': ('Název protiůčtu'),
            'rok_narozeni': ('Rok narození'),
        }
        error_messages = {
            'username': {
                'unique': ('The username is not available')
            },
            'first_name': {
                'required': ('The field can not be empty')
            },
            'last_name': {
                'required': ('The field can not be empty')
            },
            'password': {
                'required': ('The field can not be empty')
            }

        }

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
