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

from django.contrib import admin
from django import forms
from .models import Clen, Akce, Ucastnici, Film, Zanr, Tag, Uzivatel, UzivatelManager, Prichozi_platby, Naplanovane_platby #Importujeme si modely
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UzivatelCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Uzivatel
        fields = ['email']

    def save(self, commit=True):
        if self.is_valid():
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user
			
			
class UzivatelChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = Uzivatel
        fields = ['email', 'is_admin']
		
    def __init__(self, *args, **kwargs):
        super(UzivatelChangeForm, self).__init__(*args, **kwargs)
        self.Meta.fields.remove('password')

		
class UzivatelAdmin(UserAdmin):
    form = UzivatelChangeForm
    add_form = UzivatelCreationForm

    list_display = ['email', 'is_admin']
    list_filter = ['is_admin']
    fieldsets = (
        (None, {'fields': ['email', 'password']}),
        ('Permissions', {'fields': ['is_admin']}),
    )

    add_fieldsets = (
        (None, {
            'fields': ['email', 'password']}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = []		
			

#Modely registrujeme
admin.site.register(Clen)
admin.site.register(Prichozi_platby)
admin.site.register(Naplanovane_platby)
admin.site.register(Akce)
admin.site.register(Film)
admin.site.register(Zanr)
admin.site.register(Ucastnici)
admin.site.register(Uzivatel, UzivatelAdmin)
admin.site.register(Tag)