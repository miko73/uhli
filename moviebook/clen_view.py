from django.shortcuts import render
from django.views import generic

from .models import Zanr, Film, Uzivatel, Clen, Prichozi_platby, Naplanovane_platby
from .forms import FilmForm, ZanrForm, UzivatelForm, LoginForm, ClenForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class ClenIndex(generic.ListView):
    template_name = "moviebook/clen_index.html"  # cesta k templatu ze složky templates (je možné sdílet mezi aplikacemi)
    context_object_name = "clenove"  # pod tímto jménem budeme volat list objektů v templatu

    # tato funkce nám získává list filmů od největšího id (9,8,7...)
    def get_queryset(self):
        return Clen.objects.all().order_by("-id")

class CurrentClenView(generic.DetailView):
    model = Clen
    template_name = "moviebook/clen_detail.html"

    def get(self, request, pk):
        try:
            clen = self.get_object()
        except:
            return redirect("clenove_index")
        return render(request, self.template_name, {"clen": clen})

    def post(self, request, pk):
        if request.user.is_authenticated:
            if "edit_clen" in request.POST:
                return redirect("edit_clen", pk=self.get_object().pk)
            if "db_tests" in request.POST:
                return redirect("db_tests", pk=self.get_object().pk)
            if "delete_clen" in request.POST:
                if not request.user.is_admin:
                    messages.info(request, "Nemáš práva pro smazání člena.")
                    return redirect(reverse("clenove_index"))
                else:
                    self.get_object().delete()
        return redirect(reverse("clenove_index"))


class CreateClen(LoginRequiredMixin, generic.edit.CreateView):
    form_class = ClenForm
    template_name = "moviebook/create_clen.html"

    # Metoda pro GET request, zobrazí pouze formulár
    def get(self, request):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro pridání clena.")
            return redirect(reverse("clenove_index"))
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    # Metoda pro POST request, zkontroluje formulár, pokud je validní vytvorí nový clen, pokud ne zobrazí formulár s chybovou hláškou
    def post(self, request):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro pridání člena.")
            return redirect(reverse("clenove_index"))
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("clenove_index")
        return render(request, self.template_name, {"form": form})


class EditClen(LoginRequiredMixin, generic.edit.CreateView):
    form_class = ClenForm
    template_name = "moviebook/create_clen.html"

    def get(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro úpravu clena.")
            return redirect(reverse("clenove_index"))
        try:
            clen = Clen.objects.get(pk=pk)
        except:
            messages.error(request, "Tento clen neexistuje!")
            return redirect("clenove_index")
        form = self.form_class(instance=clen)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro úpravu žánru.")
            return redirect(reverse("clenove_index"))
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            rc = form.cleaned_data["rc"]
            #narozen = form.cleaned_data["narozen"]
            jmeno = form.cleaned_data["jmeno"]
            prijmeni = form.cleaned_data["prijmeni"]
            #prijmeni = "prijmeni"
            try:
                clen = Clen.objects.get(pk=pk)
            except:
                messages.error(request, "Tento člen neexistuje!")
                return redirect(reverse("clenove_index"))
            clen.email = email
            clen.rc = rc
            #clen.narozen = narozen
            clen.jmeno = jmeno
            clen.prijmeni = prijmeni
            clen.save()
        else:
            messages.info(request, "Chyba ve formuláři")
        #    return redirect(reverse(form.errors))
        # return render(request, self.template_name, {"form":form})
        #return redirect("clen_detail", pk=ret_id)
        return redirect("clen_detail", pk=pk)


