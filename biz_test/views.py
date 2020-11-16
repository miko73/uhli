from django.shortcuts import render
from . import biz_modul
from django.views import generic
from django import forms
from .models import UsageAddresList

class UALview(generic.ListView):
    template_name = "biz/UsageList_index.html"  # cesta k templatu ze složky templates (je možné sdílet mezi aplikacemi)
    context_object_name = "UsageLabels"  # pod tímto jménem budeme volat list objektů v templatu

# tato funkce nám získává list UAL od největšího id (9,8,7...)
    def get_queryset(self):
        return UsageAddresList.objects.all().order_by("-id")


def biz1(request):
    error_msg = "Tady"
    vysledek = "None"
    usage_list = biz_modul.get_result("select UsageCode, UsageLabel from UsageAddresList;")
    if request.method == "POST":
            try:
                query = request.POST["a"]
            except:
                error_msg = "Byl jsem v exception a query bylo {}".format(query)
                return render(request, "biz/Karlin1.html", dict(error_msg=error_msg, usages=usage_list, row="test1,test2,test3"))
            #vysledek = query
            vysledek = biz_modul.get_result(query)

            #[(1, 'průmyslový objekt'), (3, 'objekt k bydlení'), (5, 'objekt občanské vybavenosti'), (6, 'bytový dům'), (7, 'rodinný dům'), (10, 'stavba pro obchod'), (11, 'stavba ubytovacího zařízení'), (12, 'stavba pro výrobu a skladování'), (14, 'stavba pro administrativu'), (15, 'stavba občanského vybavení'), (17, 'stavba pro dopravu'), (19, 'jiná stavba'), (20, 'víceúčelová stavba')]
            return render(request, "biz/Karlin1.html", dict(error_msg=error_msg, usages=usage_list, rows=vysledek))
    error_msg = "ani nic"
    return render(request, "biz/Karlin1.html", dict(error_msg=error_msg, usages=usage_list, rows=vysledek))

