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

from django.shortcuts import render
from django.views import generic

from .models import Zanr, Film, Uzivatel, Clen
from .forms import FilmForm, ZanrForm,  ClenForm, UzivatelForm, LoginForm
from .clen_view import ClenIndex, CurrentClenView, CreateClen, EditClen

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class FilmIndex(generic.ListView):

    template_name = "moviebook/film_index.html" # cesta k templatu ze složky templates (je možné sdílet mezi aplikacemi)
    context_object_name = "filmy" # pod tímto jménem budeme volat list objektů v templatu

# tato funkce nám získává list filmů od největšího id (9,8,7...)
    def get_queryset(self):
        return Film.objects.all().order_by("-id")

		
class CurrentFilmView(generic.DetailView):

    model = Film
    template_name = "moviebook/film_detail.html"
	
    def get(self, request, pk):
        try:
            film = self.get_object()
        except:
            return redirect("filmovy_index")
        return render(request, self.template_name, {"film" : film})
		
    def post(self, request, pk):
        if request.user.is_authenticated:
            if "edit_film" in request.POST:
                return redirect("edit_film", pk=self.get_object().pk)
            else:
                if not request.user.is_admin:
                    messages.info(request, "Nemáš práva pro smazání filmu.")
                    return redirect(reverse("filmovy_index"))
                else:
                    self.get_object().delete()
        return redirect(reverse("filmovy_index"))
	
class CreateFilm(LoginRequiredMixin, generic.edit.CreateView):

    form_class = FilmForm
    template_name = "moviebook/create_film.html"

    # Metoda pro GET request, zobrazí pouze formulář
    def get(self, request):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro přidání filmu.")
            return redirect(reverse("filmovy_index"))
        form = self.form_class(None)
        return render(request, self.template_name, {"form":form})

    # Metoda pro POST request, zkontroluje formulář, pokud je validní vytvoří nový film, pokud ne zobrazí formulář s chybovou hláškou
    def post(self, request):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro přidání filmu.")
            return redirect(reverse("filmovy_index"))			
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("filmovy_index")
        return render(request, self.template_name, {"form":form})
		
class EditFilm(LoginRequiredMixin, generic.edit.CreateView):
    form_class = FilmForm
    template_name = "moviebook/create_film.html"
	
    def get(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro úpravu filmu.")
            return redirect(reverse("filmovy_index"))
        try:
            film = Film.objects.get(pk = pk)
        except:
            messages.error(request, "Tento film neexistuje!")
            return redirect("filmovy_index")
        form = self.form_class(instance=film)
        return render(request, self.template_name, {"form":form})

    def post(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro úpravu filmu.")
            return redirect(reverse("filmovy_index"))
        form = self.form_class(request.POST)

        if form.is_valid():
            nazev = form.cleaned_data["nazev"]
            rezie = form.cleaned_data["rezie"]
            zanr = form.cleaned_data["zanr"]
            tagy = form.cleaned_data["tagy"]
            try:
                film = Film.objects.get(pk = pk)
            except:
                messages.error(request, "Tento film neexistuje!")
                return redirect(reverse("filmovy_index"))
            film.nazev = nazev
            film.rezie = rezie
            film.zanr = zanr
            film.tagy.set(tagy)
            film.save()
        #return render(request, self.template_name, {"form":form})
        return redirect("filmovy_detail", pk = film.id)

class ZanrIndex(generic.ListView):

    template_name = "moviebook/zanr_index.html" # cesta k templatu ze složky templates (je možné sdílet mezi aplikacemi)
    context_object_name = "zanry" # pod tímto jménem budeme volat list objektů v templatu

# tato funkce nám získává list filmů od největšího id (9,8,7...)
    def get_queryset(self):
        return Zanr.objects.all().order_by("-id")

class CurrentZanrView(generic.DetailView):

    model = Zanr
    template_name = "moviebook/zanr_detail.html"
	
    def get(self, request, pk):
        try:
            zanr = self.get_object()
        except:
            return redirect("zanrovy_index")
        return render(request, self.template_name, {"zanr" : zanr})
		
    def post(self, request, pk):
        if request.user.is_authenticated:
            if "edit_zanr" in request.POST:
                return redirect("edit_zanr", pk=self.get_object().pk)
            else:
                if not request.user.is_admin:
                    messages.info(request, "Nemáš práva pro smazání zanru.")
                    return redirect(reverse("zanrovy_index"))
                else:
                    self.get_object().delete()
        return redirect(reverse("zanrovy_index"))
		
class CreateZanr(LoginRequiredMixin, generic.edit.CreateView):

    form_class = ZanrForm
    template_name = "moviebook/create_zanr.html"

    # Metoda pro GET request, zobrazí pouze formulár
    def get(self, request):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro pridání zanru.")
            return redirect(reverse("zanrovy_index"))
        form = self.form_class(None)
        return render(request, self.template_name, {"form":form})

    # Metoda pro POST request, zkontroluje formulár, pokud je validní vytvorí nový zanr, pokud ne zobrazí formulár s chybovou hláškou
    def post(self, request):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro pridání zanru.")
            return redirect(reverse("zanrovy_index"))			
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("zanrovy_index")
        return render(request, self.template_name, {"form":form})

class EditZanr(LoginRequiredMixin, generic.edit.CreateView):
    form_class = ZanrForm
    template_name = "moviebook/create_zanr.html"
	
    def get(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro úpravu zanru.")
            return redirect(reverse("zanrovy_index"))
        try:
            zanr = Zanr.objects.get(pk = pk)
        except:
            messages.error(request, "Tento zanr neexistuje!")
            return redirect("zanrovy_index")
        form = self.form_class(instance=zanr)
        return render(request, self.template_name, {"form":form})

    def post(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro úpravu žánru.")
            return redirect(reverse("zanrovy_index"))
        form = self.form_class(request.POST)
        if form.is_valid():
            nazev_zanru = form.cleaned_data["nazev_zanru"]
            try:
                zanr = Zanr.objects.get(pk = pk)
            except:
                messages.error(request, "Tento žánr neexistuje!")
                return redirect(reverse("zanrovy_index"))
            zanr.nazev_zanru = nazev_zanru
            zanr.save()
        #return render(request, self.template_name, {"form":form})
        return redirect("zanrovy_detail", pk = zanr.id)


class UzivatelViewRegister(generic.edit.CreateView):
    form_class = UzivatelForm
    model = Uzivatel
    template_name = "moviebook/user_form.html"

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Už jsi přihlášený, nemůžeš se registrovat.")
            return redirect(reverse("filmovy_index"))            
        else:
            form = self.form_class(None)
        return render(request, self.template_name, {"form":form})

    def post(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Už jsi přihlášený, nemůžeš se registrovat.")
            return redirect(reverse("filmovy_index"))
        form = self.form_class(request.POST)
        if form.is_valid():
            uzivatel = form.save(commit = False)
            password = form.cleaned_data["password"]
            uzivatel.set_password(password)
            uzivatel.save()
            login(request, uzivatel)
            return redirect("filmovy_index")
            
        return render(request, self.template_name, {"form":form})

class UzivatelViewLogin(generic.edit.CreateView):
    form_class = LoginForm
    template_name = "moviebook/user_form.html"

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Už jsi přihlášený, nemůžeš se přihlásit znovu.")
            return redirect(reverse("filmovy_index"))
        else:
            form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Už jsi přihlášený, nemůžeš se přihlásit znovu.")
            return redirect(reverse("filmovy_index"))
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email = email, password = password)
            if user:
                login(request, user)
                return redirect("filmovy_index")
            else:
                messages.error(request, "Tento účet neexistuje.")
        return render(request, self.template_name, {"form": form})
		
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        messages.info(request, "Nemůžeš se odhlásit, pokud nejsi přihlášený.")
    return redirect(reverse("login"))

class DbTestClen(generic.DetailView):
    model = Clen
    template_name = "moviebook/dbtest_detail.html"

    def get(self, request, pk):
        try:
            clen = self.get_object()
        except:
            return redirect("clenove_index")
        return render(request, self.template_name, {"clen": clen})

    def post(self, request, pk):
        if "edit_clen" in request.POST:

            c1 = Clen.objects.create(narozen="2012-07-25", clenem_od = "2020-12-24")
            c1.jmeno = "Tobiáš"
            c1.prijmeni = "Kočandrle"
            c1.rc = "123567"
            c1.clenem_od = "2020-12-24"
            c1.narozen = "2012-07-25"
            c1.facr_id = 10
            c1.klub_id = 1050181
            c1.var_symbol = 122
            c1.save()
            del c1
            return redirect("clenove_index")


            #return redirect(reverse("clenove_index"))
        if "delete_clen" in request.POST:
            return redirect("clenove_index")
#                    return redirect(reverse("clenove_index"))
        else:
#                   self.get_object().delete()
            return redirect("clenove_index")