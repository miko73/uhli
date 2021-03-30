from django.shortcuts import render
from django.views import generic

from .models import Zanr, Film, Uzivatel, Clen, Prichozi_platby, Naplanovane_platby
from .forms import FilmForm, ZanrForm, UzivatelForm, LoginForm, ClenForm, PlatbaForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render


#######################################
# Platba
#######################################

def PlatbaIndex(request):
    # qs = Platba_list = Prichozi_platby.objects.all()
    qs = Prichozi_platby.objects.all()
    platba_contains_query = request.GET.get('title_contains')
    
    # print("title_contains_query - {0}".format(title_contains_query))
    if platba_contains_query != '' and platba_contains_query is not None:
    # qs = qs.filter(facr_id__icontains=9090086)
        qs = qs.filter(zprava_pro_prijemce__icontains=platba_contains_query)
    print(qs)

    context = {
        'platba_qs': qs
    } 
    return render(request, "moviebook/platba_index.html", context)

##############################
class CurrentPlatbaView(generic.edit.CreateView):
    model = Prichozi_platby
    form_class = PlatbaForm
    template_name = "moviebook/platba_detail.html"
    def get(self, request, pk):
        try:
            platba = Prichozi_platby.objects.get(pk=pk)
        except:
            return redirect("platba_index")
        
        form = self.form_class(instance=platba)
        
        # print(f'facr_id_query {facr_id_query}')
        
        context = {
        'form':form
        }
        # return render(request, self.template_name, {"form": form })
        # return render(request, self.template_name, {"form": form, "platby":qs_platby})
        return render(request, self.template_name, context)


    def post(self, request, pk):
        if request.user.is_authenticated:
            if "edit_platba" in request.POST:
                return redirect("edit_platba", pk=self.get_object().pk)
            if "delete_platba" in request.POST:
                if not request.user.is_admin:
                    messages.info(request, "Nemáš práva pro smazání člena.")
                    return redirect(reverse("clenove_index"))
                else:
                    self.get_object().delete()
        return redirect(reverse("platba_index"))


class EditPlatba(LoginRequiredMixin, generic.edit.UpdateView):
    form_class = PlatbaForm
    template_name = "moviebook/edit_platba.html"


    def get(self, request, pk):        
        print (f'request.GET {request.GET}')
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro úpravu.")
            return redirect(reverse("platba_index"))
        try:
            platba = Prichozi_platby.objects.get(pk=pk)
            print(f'pk.id')
        except:
            messages.error(request, "Platba neexistuje!")
            return redirect("platba_index")

        print ("EDIT PLATBA")
        form = self.form_class(instance=platba)
        

########################################################################
        qs = Clen_list = Clen.objects.all()
        filter_prijmeni = request.GET.get('filter_prijmeni')
        clen_detail =  request.GET.get('clen_detail')
        # print("title_contains_query - {0}".format(title_contains_query))
        # print(f'filter_prijmeni {filter_prijmeni}')
        # print(f'platba.prijmeni {platba.prijmeni}')

        if filter_prijmeni != '' and filter_prijmeni is not None:   
            qs = qs.filter(prijmeni__icontains=filter_prijmeni)       
        elif platba.prijmeni is not None:
            qs = qs.filter(prijmeni__icontains=platba.prijmeni)

        context = {
            'form': form,
            'clen_qs': qs
        }
        print ("filter_prijmeni ", filter_prijmeni)
        print ("clen detail ", clen_detail) 
########################################################################



        return render(request, self.template_name, context)



    def post(self, request, pk):
        print (f'request.POST {request.POST}')
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro úpravu")
            return redirect(reverse("platba_index"))
        context = {}
        platba = Prichozi_platby.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=platba) # Here is the difference between insert and updte instance=clen has to be passed as imput parameter            
        if form.is_valid():
            try:
                form.save()
                messages.info(request, "SAVED !!!")
            except:
                messages.error(request, "Can not save")
        else:
            messages.info(request, "Chyba ve formuláři ")
        return render(request, self.template_name, {"form":form})
#######################################
# Clen
#######################################


def ClenIndex(request):
    qs = Clen_list = Clen.objects.all()
    title_contains_query = request.GET.get('title_contains')
    # print("title_contains_query - {0}".format(title_contains_query))

    if title_contains_query != '' and title_contains_query is not None:
        qs = qs.filter(prijmeni__icontains=title_contains_query)        

    context = {
        'clen_qs': qs
    }
    print ("in ClenIndex")
    return render(request, "moviebook/clen_index.html", context)




# class CurrentClenView(generic.DetailView):
class CurrentClenView(generic.edit.CreateView):
    model = Clen
    form_class = ClenForm
    template_name = "moviebook/clen_detail.html"

    def get(self, request, pk):
        try:
            clen = Clen.objects.get(pk=pk)
            # platby = Clen.objects.all()
            # platby = platby.filter(clen__in=clen.var_symbol )

            # qs_platby = Prichozi_platby.objects.all()
            facr_id_query = clen.facr_id
            qs_platby = Prichozi_platby.objects.all()
            qs_platby = qs_platby.filter(facr_id__icontains=facr_id_query)
            # qs_platby = qs_platby.filter(facr_id__icontains=facr_id_query)
    
            global actual_id_clen
            actual_id_clen = clen.id
            print (f'actual_id_clen {actual_id_clen}')
            # for platba in qs_platby:
            # print (len(qs_platby))
        except:
            return redirect("clenove_index")
        
        form = self.form_class(instance=clen)
        
        # print(f'facr_id_query {facr_id_query}')
        
        context = {
        'form':form,
        'platba_qs':qs_platby
        }
        # return render(request, self.template_name, {"form": form })
        # return render(request, self.template_name, {"form": form, "platby":qs_platby})
        return render(request, self.template_name, context)


    def post(self, request, pk):
        if request.user.is_authenticated:
            if "edit_clen" in request.POST:
                return redirect("edit_clen", pk=self.get_object().pk)
            if "select_clen" in request.POST:
                return redirect(reverse("clenove_index"))
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
        if "Save_clen" in request.POST:
            if form.is_valid():
                try:
                    if clen.var_symbol == 1:
                        clen.var_symbol = clen.id
                    if clen.facr_id == 1:
                        clen.facr_id = clen.id                        
                    form.save()
                    messages.info(request, "SAVED !!! clen.var_symbol {clen.var_symbol}")
                except:
                    messages.error(request, "Can not save")
            else:
                messages.info(request, "Chyba ve formuláři {0}".format(form.cleaned_data["narozen"]))
                return render(request, self.template_name, {"form":form})
                        
        if "Back_clen" in request.POST:
            return redirect("clen_detail", pk = clen.id)

        # print (f'request.POST {request.POST}')
        return redirect("clen_detail", pk = clen.id)
            # return redirect("filmovy_detail", pk = film.id)
            # return redirect("clen_detail", pk=pk)



        



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


