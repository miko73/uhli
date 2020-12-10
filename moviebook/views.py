
from django.shortcuts import render
from django.views import generic

from .models import Zanr, Film, Uzivatel, Clen
from .forms import FilmForm, ZanrForm,  ClenForm, UzivatelForm, LoginForm
from .clen_view import ClenIndex, CurrentClenView, CreateClen, EditClen, Prichozi_platby, PlatbaIndex, CurrentPlatbaView, EditPlatba


from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import csv

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



def load_vypis():
    # dbcon = create_connection("../db.sqlite3")
    with open('C:\\Users\\micha\\Projects\\uhli\\Pohyby_na_uctu-2000679390_20160101-20201201.csv', encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # print(f'\t{row[0]},{row[1]},{row[2]},{row[4]},{row[5]},{row[6]},{row[7]}')
                
                platba = Prichozi_platby(row[0],row[1],row[2],row[4],row[5],row[6],row[7])
                print (platba)
                platba.save()

                line_count += 1
            if line_count > 10:
                break

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
        try:
            clen = self.get_object()
        except:
            return redirect("clenove_index")


        if "test1" in request.POST:
             load_vypis()
        if "test2" in request.POST:
            pass
        if "test3" in request.POST:
            pass
        return render(request, self.template_name, {"clen": clen})
