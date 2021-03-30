from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

class StaticVariables:
    actual_id_platba = 0
    actual_id_clen = 0
    def __str__(self):
        return "actual_id_platba: {0} | actual_id_clen: {1}".format(self.actual_id_platba, self.actual_id_clen)



class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''

class Clen (models.Model):
    email = models.EmailField(max_length = 300, null=True, blank=True, default="", unique=False)
    rc = models.CharField(max_length=10, null=True, blank=True, default="", unique=False)
    # narozen = models.DateTimeField(null=True, blank=True)
    # narozen = models.DateTimeField(null=True, blank=True)
    # narozen = CustomDateTimeField(auto_now_add=True)
    clenem_od = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True, blank=True)
    jmeno = models.CharField(max_length = 40, null=True, blank=True, default="", unique=False)
    prijmeni = models.CharField(max_length = 40, null=True, blank=True, default="", unique=False)
    prijmeni_rodic = models.CharField(max_length = 40, null=True, blank=True, default="", unique=False)
    facr_id = models.IntegerField (default=1)
    var_symbol = models.IntegerField (default=1)
    klub_id = models.IntegerField (default=10)
    cislo_uctu = models.CharField(max_length=30, null=True, blank=True, default="", unique=False)
    telefonni_cislo = models.CharField(max_length=30, null=True, blank=True, default="", unique=False)
    typ_clena = models.CharField(max_length=20, null=True, blank=True, default="", unique=False)
    ucet_protiucet = models.CharField(max_length=20, null=True, blank=True, default="", unique=False)
    ucet_protiucet2 = models.CharField(max_length=20, null=True, blank=True, default="", unique=False)
    ucet_kod_banky = models.CharField(max_length=6, null=True, blank=True, default="", unique=False)
    ucet_zprava_pro_prijemce = models.CharField(max_length=160, null=True, blank=True, default="", unique=False)
    ucet_poznamka = models.CharField(max_length=160, null=True, blank=True, default="", unique=False)
    ucet_nazev_protiuctu = models.CharField(max_length=100, null=True, blank=True, default="", unique=False)
    rok_narozeni = models.CharField(max_length=4, null=True, blank=True, default="", unique=False )


    def __str__(self):
        return "Jméno: {0} | Príjemní: {1} | email {2} ".format(self.jmeno, self.prijmeni, self.email, self.rok_narozeni)

    class Meta:
        verbose_name = "Clen"
        verbose_name_plural = "Clenové"


# class ClenFilter(django_filters.FilterSet):
#     class Meta:
#         model = Clen
#         fields = ['prijmeni', ]


class Prichozi_platby(models.Model):
    datum = models.DateField( null=True)
    # datum = models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    objem = models.FloatField( null=True)
    protiucet= models.CharField(max_length=100, null=True, default="", unique=False)
    kod_banky = models.CharField(max_length=6, null=True, default="", unique=False)
    zprava_pro_prijemce = models.CharField(max_length=160, null=True, default="", unique=False)
    poznamka = models.CharField(max_length=160, null= True,blank=True, default="", unique=False)
    nazev_protiuctu = models.CharField(max_length=100, null=True, blank=True, default="", unique=False)
    typ_platby = models.CharField(max_length=30, null=True, default="", unique=False)
    cislo_uctu_prichozi = models.CharField(max_length=20, null=True ,blank=True, default="", unique=False)
    jmeno = models.CharField(max_length=20, null=True , default="", unique=False)
    prijmeni = models.CharField(max_length=20, null=True , default="", unique=False)
    facr_id = models.IntegerField (default=1)
    
    # ﻿"Datum", Objem, Měna, Protiúčet, Kód banky, Zpráva pro příjemce, Poznámka, Typ
    # def __init__(self, datum, objem, protiucet, kod_banky, zprava_pro_prijemce, poznamka, typ_platby):
    #     self.datum = datum
    #     self.objem = objem
    #     self.protiucet=protiucet
    #     self.kod_banky=kod_banky 
    #     self.zprava_pro_prijemce=zprava_pro_prijemce
    #     self.poznamka=poznamka
    #     # self.nazev_protiuctu=nazev_protiuctu
    #     self.typ_platby=typ_platby
    #     # self.cislo_uctu_prichozi=cislo_uctu_prichozi
    #     # self.clen=clen


    def __str__(self):
        return "Částka {0} | Poznámka {1}".format(self.objem, self.poznamka)
        # return "Datum: {0} | Částka {1} | Poznámka {2}".format(self.datum, self.objem, self.poznamka)

    class Metadata:
        verbose_name = "Platba"
        verbose_name_plural = "Platby"

class Naplanovane_platby(models.Model):
    splatnost = models.DateField(null=True)
    objem = models.FloatField(null=True)
    popis_platby = models.CharField(max_length=160, null=True, default="", unique=False)
    sdelelni = models.CharField(max_length=160, null=True, default="", unique=False)
    clen = models.ForeignKey(Clen, on_delete=models.SET_NULL,null=True, related_name = "clen_np", verbose_name="Člen")
    trener = models.ForeignKey(Clen, on_delete=models.SET_NULL,null=True, related_name = "trener", verbose_name="Trenér")
    sparovano = models.ForeignKey(Prichozi_platby, on_delete=models.SET_NULL,null=True, related_name = "parovani", verbose_name="Párování")

    def __str__(self):
        return "splatnos: {0} | Částka {1} | Popis {2}".format(self.splatnost, self.objem, self.popis_platby)

    class Metadata:
        verbose_name = "Naplánovana_Platba"
        verbose_name_plural = "Naplánovane Platby"

class Akce(models.Model):
    nazev_akce = models.CharField(max_length=80, null=True, verbose_name="Název akce")
    datum_konani = models.DateTimeField(null=True)
    vedouci = models.ForeignKey(Clen, on_delete=models.SET_NULL,null=True, related_name = "vedoucip", verbose_name="Vedouci")
    trener = models.ForeignKey(Clen, on_delete=models.SET_NULL,null=True, related_name = "trenerp", verbose_name="trener")
    
    def kdy(self):
        return self.datum_konani.isoformat()
        
    def __str__(self):
        return "Nazev_akce: {0} | Konání: {1}".format(self.nazev_akce, self.datum_konani.isoformat())

    class Meta:
        verbose_name="Akce"
        verbose_name_plural="Akce"
 

class Ucastnici(models.Model):
    akce = models.ForeignKey(Akce, on_delete=models.SET_NULL, null=True, verbose_name="Akce")
    clen = models.ForeignKey(Clen, on_delete=models.SET_NULL,null=True, verbose_name="Clen")
          
    def __str__(self):
        return "Akce: {0} | Datum: {1} | Ucastník: {2} ".format(akce.nazev_akce, self.akce.datum_konani.isoformat(), self.clen.jmeno, self.clen.prijmeni)

    class Meta:
        verbose_name = "Úcastník"
        verbose_name_plural = "Úcastníci"
 
class Zanr(models.Model):
    nazev_zanru = models.CharField(max_length=80, null=True, verbose_name="Žánr")

    def __str__(self):
        return "Nazev_zanru: {0}".format(self.nazev_zanru)

    class Meta:
        verbose_name="Žánr"
        verbose_name_plural="Žánry"
		
class Tag(models.Model):
    tag_title = models.CharField(max_length = 30, null=True, verbose_name="Tagy")

    def __str__(self):
        return self.tag_title

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tagy"		

class Film(models.Model):
    nazev = models.CharField(max_length=200, verbose_name="Název Filmu")
    rezie = models.CharField(max_length=180, verbose_name="Režie")
    zanr = models.ForeignKey(Zanr, on_delete=models.SET_NULL, null=True, verbose_name="Žánr")
    tagy = models.ManyToManyField(Tag)
	
    def __init__(self, *args, **kwargs):
        super(Film, self).__init__(*args, **kwargs)
		
    def __str__(self):
        tags = [i.tag_title for i in self.tagy.all()]
        return "Nazev: {0} | Rezie: {1} | Zanr: {2} | Tagy: {3}".format(self.nazev, self.rezie, self.zanr.nazev_zanru, tags)

    class Meta:
        verbose_name="Film"
        verbose_name_plural="Filmy"
	
class UzivatelManager(BaseUserManager):
    # Vytvoří uživatele
    def create_user(self, email, password):
        print(self.model)
        if email and password:
            user = self.model(email=self.normalize_email(email))
            user.set_password(password)
            user.save()
        return user
    # Vytvoří admina
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save()
        return user
		
class Uzivatel(AbstractBaseUser):

    email = models.EmailField(max_length = 300, unique=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = "uživatel"
        verbose_name_plural = "uživatelé"

    objects = UzivatelManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return "email: {}".format(self.email)
    
    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True	