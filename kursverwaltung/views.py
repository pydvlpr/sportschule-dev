from django.shortcuts import get_object_or_404,render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

from .models.kunde import Kunde
from .models.trainer import Trainer
from .models.kurs import Kurs
from .models.raum import Raum
from .models.buchung import Buchung
from .models.zertifizierung import Zertifizierung


class KundeErstellen(CreateView):
    model = Kunde
    fiels = [   'nachname', 'vorname', 'strasse',
                'hausnummer', 'plz', 'stadt',
                'handy','festnetz','fax', 'e_mail',
                'ansprechpartner'
             ]

class KundeAktualisieren(UpdateView):
     model = Kunde
     fiels = [   'nachname', 'vorname', 'strasse',
                 'hausnummer', 'plz', 'stadt',
                 'handy','festnetz','fax', 'e_mail',
                 'ansprechpartner'
              ]


class KundeLoeschen(DeleteView):
    model = Kunde
    success_url = reverse_lazy('kunden_liste')

# Index-Site
def index(request):
    return render(request, 'kursverwaltung/index.html')

# Kurs Views
def kurs_liste(request):
    #kurs_liste = Kurse.objects.order_by('id')
    #context = {'kurs_liste':course_list}
    #return render(request, 'kursverwaltung/kurs-liste.html',context)
    return render(request, 'kursverwaltung/kurs-liste.html')

# Trainer Views
def trainer_liste(request):
    #kurs_liste = Kurse.objects.order_by('id')
    #context = {'kurs_liste':course_list}
    #return render(request, 'kursverwaltung/kurs-liste.html',context)
    return render(request, 'kursverwaltung/trainer-liste.html')

# Kunden Views
def kunden_liste(request):
    #kurs_liste = Kurse.objects.order_by('id')
    #context = {'kurs_liste':course_list}
    #return render(request, 'kursverwaltung/kurs-liste.html',context)
    return render(request, 'kursverwaltung/kunden-liste.html')

# Buchungen views
def buchungen_liste(request):
    #kurs_liste = Kurse.objects.order_by('id')
    #context = {'kurs_liste':course_list}
    #return render(request, 'kursverwaltung/kurs-liste.html',context)
    return render(request, 'kursverwaltung/buchungen-liste.html')

# Räume views
def raum_liste(request):
    #kurs_liste = Kurse.objects.order_by('id')
    #context = {'kurs_liste':course_list}
    #return render(request, 'kursverwaltung/kurs-liste.html',context)
    return render(request, 'kursverwaltung/raum-liste.html')
    # Kunden Views

# Zertfifizierungen views
def zertifizierung_liste(request):
    #kurs_liste = Kurse.objects.order_by('id')
    #context = {'kurs_liste':course_list}
    #return render(request, 'kursverwaltung/kurs-liste.html',context)
    return render(request, 'kursverwaltung/zertifizierung-liste.html')
    # Kunden Views
