from django.shortcuts import get_object_or_404,render, redirect
from django.urls import reverse_lazy, reverse
from django import forms
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

from .models.kunde import Kunde
from .models.trainer import Trainer
from .models.kurs import Kurs
from .models.raum import Raum
from .models.buchung import Buchung
from .models.zertifizierung import Zertifizierung

## Index-Site
# kann später ggf. entfernt werden

def index(request):
    return render(request, 'kursverwaltung/index.html')

## Kunden Views

def kunden_liste(request):
    kunden_liste = Kunde.objects.order_by('id')
    context = {'kunden_liste':kunden_liste}
    return render(request, 'kursverwaltung/kunden-liste.html',context)


class KundeErstellen(CreateView):
    template_name = "kunde_create_form.html"
    model = Kunde

    fields = [   'nachname', 'vorname', 'strasse',
                'hausnummer', 'plz', 'stadt',
                'handy','festnetz','fax', 'e_mail',
                'ansprechpartner',
             ]
    success_url = reverse_lazy('kunden_liste')

    def get_form(self, form_class=None):
        form = super(KundeErstellen, self).get_form(form_class)
        form.fields['handy'].required = False
        form.fields['fax'].required = False
        return form

class KundeAktualisieren(UpdateView):

    model = Kunde
    fields = [   'nachname', 'vorname', 'strasse',
                 'hausnummer', 'plz', 'stadt',
                 'handy','festnetz','fax', 'e_mail',
                 'ansprechpartner'
              ]
    template_name_suffix = '_aktualisieren_form'
    success_url = reverse_lazy('kunden_liste')

    def get_form(self, form_class=None):
        form = super(KundeAktualisieren, self).get_form(form_class)
        form.fields['handy'].required = False
        form.fields['fax'].required = False
        return form


class KundeEntfernen(DeleteView):
    model = Kunde
    success_url = reverse_lazy('kunden_liste')


## Trainer Views

def trainer_liste(request):
    trainer_liste = Trainer.objects.order_by('id')
    context = {'trainer_liste':trainer_liste}
    return render(request, 'kursverwaltung/trainer-liste.html',context)

class TrainerErstellen(CreateView):
    template_name = "trainer_create_form.html"
    model = Trainer

    fields = [   'nachname', 'vorname', 'geb_datum', 'strasse',
                'hausnummer', 'plz', 'stadt',
                'festnetz', 'e_mail',
                'bemerkung', 'zertifizierung'
             ]
    success_url = reverse_lazy('trainer_liste')

    def get_form(self, form_class=None):
        form = super(TrainerErstellen, self).get_form(form_class)
        form.fields['bemerkung'].required = False
        form.fields['zertifizierung'].required = False #später entfernen, soll True sein!
        return form

    class Meta:
        widgets = {
            'note': forms.Textarea(attrs={'cols' :25, 'row':    100}),
            }


class TrainerAktualisieren(UpdateView):

    model = Trainer
    fields = [   'nachname', 'vorname', 'geb_datum', 'strasse',
                'hausnummer', 'plz', 'stadt',
                'festnetz', 'e_mail',
                'bemerkung', 'zertifizierung'
             ]
    template_name_suffix = '_aktualisieren_form'
    success_url = reverse_lazy('trainer_liste')

    def get_form(self, form_class=None):
        form = super(TrainerAktualisieren, self).get_form(form_class)
        form.fields['bemerkung'].required = False
        form.fields['zertifizierung'].required = False #später entfernen, soll True sein!
        return form

    class Meta:
        widgets = {
            'note': forms.Textarea(attrs={'cols' :25, 'row':    100})
            },

class TrainerEntfernen(DeleteView):
    model = Trainer
    success_url = reverse_lazy('trainer_liste')



## Zertfifizierungen views
def zertifizierung_liste(request):

    return render(request, 'kursverwaltung/zertifizierung-liste.html')



## Kurs Views

def kurs_liste(request):

    return render(request, 'kursverwaltung/kurs-liste.html')


## Buchungen views
def buchungen_liste(request):

    return render(request, 'kursverwaltung/buchungen-liste.html')


## Räume views
def raum_liste(request):

    return render(request, 'kursverwaltung/raum-liste.html')
    # Kunden Views
