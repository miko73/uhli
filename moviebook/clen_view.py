from django.shortcuts import render
from django.views import generic

from .models import Zanr, Film, Uzivatel, Clen, Prichozi_platby, Naplanovane_platby
from .forms import FilmForm, ZanrForm, UzivatelForm, LoginForm, ClenForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render




def ClenIndex(request):
    qs = Clen_list = Clen.objects.all()
    title_contains_query = request.GET.get('title_contains')
    print("title_contains_query - {0}".format(title_contains_query))

    if title_contains_query != '' and title_contains_query is not None:
        qs = qs.filter(prijmeni__icontains=title_contains_query)        
    print(qs)

    # elif id_exact_query != '' and id_exact_query is not None:
    #     qs = qs.filter(id=id_exact_query)

    # elif title_or_author_query != '' and title_or_author_query is not None:
    #     qs = qs.filter(Q(title__icontains=title_or_author_query)
    #                    | Q(author__name__icontains=title_or_author_query)
    #                    ).distinct()

    context = {
        'clen_qs': qs
    }
    return render(request, "moviebook/clen_index.html", context)




# class CurrentClenView(generic.DetailView):
class CurrentClenView(generic.edit.CreateView):
    model = Clen
    form_class = ClenForm
    template_name = "moviebook/clen_detail.html"

    def get(self, request, pk):
        try:
            clen = Clen.objects.get(pk=pk)
        except:
            return redirect("clenove_index")
        
        form = self.form_class(instance=clen)

        return render(request, self.template_name, {"form": form})


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



class EditClen(LoginRequiredMixin, generic.edit.UpdateView):
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
        
        # for field in form:
        #     if field.errors:
        #         form.fields[field.name].widget.attrs['class'] = 'form-control is-invalid'
        
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro úpravu žánru.")
            return redirect(reverse("clenove_index"))
        context = {}
        clen = Clen.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=clen) # Here is the difference between insert and updte instance=clen has to be passed as imput parameter            
        if form.is_valid():
            try:
                form.save()
                messages.info(request, "SAVED !!!")
            except:
                messages.error(request, "Can not save")
        else:
            messages.info(request, "Chyba ve formuláři {0}".format(form.cleaned_data["narozen"]))
        return render(request, self.template_name, {"form":form})



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



class EditClen2(LoginRequiredMixin, generic.edit.CreateView):
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
            narozen = form.cleaned_data["narozen"]
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
            clen.narozen = narozen
            clen.jmeno = jmeno
            clen.prijmeni = prijmeni
            clen.save()
        else:
            messages.info(request, "Chyba ve formuláři {0}".format(form.cleaned_data["narozen"]))
        #    return redirect(reverse(form.errors))
        # return render(request, self.template_name, {"form":form})
        #return redirect("clen_detail", pk=ret_id)
        return redirect("clen_detail", pk=pk)


