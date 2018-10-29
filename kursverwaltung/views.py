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

    class Meta:
        pass

    def get_form(self, form_class=None):
        form = super(KundeErstellen, self).get_form(form_class)
        form.fields['handy'].required = False
        form.fields['fax'].required = False
        form.fields['ansprechpartner'].widget = forms.Textarea(attrs={'cols' :5, 'rows': 2,
                                                                   'class': 'form-control'})
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

    class Meta:
        pass

    def get_form(self, form_class=None):
        form = super(KundeAktualisieren, self).get_form(form_class)
        form.fields['handy'].required = False
        form.fields['fax'].required = False
        form.fields['ansprechpartner'].widget = forms.Textarea(attrs={'cols' :5, 'rows': 2,
                                                                   'class': 'form-control'})
        return form


class KundeEntfernen(DeleteView):
    model = Kunde
    success_url = reverse_lazy('kunden_liste')


## Trainer Views

def trainer_liste(request):
    trainer_liste = Trainer.objects.order_by('id')
    zertifizierungen_liste = Zertifizierung.objects.order_by('id')
    return render(request, 'kursverwaltung/trainer-liste.html',
                  {'trainer_liste':trainer_liste, 'zertifizierungen_liste':zertifizierungen_liste})


class TrainerErstellen(CreateView):
    template_name = "trainer_create_form.html"
    model = Trainer

    fields = [   'nachname', 'vorname', 'geb_datum', 'strasse',
                'hausnummer', 'plz', 'stadt',
                'festnetz', 'e_mail',
                'bemerkung'
             ]
    success_url = reverse_lazy('trainer_liste')

    class Meta:
        pass

    def get_form(self, form_class=None):
        form = super(TrainerErstellen, self).get_form(form_class)
        form.fields['geb_datum'].widget = forms.DateInput(format=('%d.%m.%Y %H:%M'),
                                                          attrs={'id':'datepicker-geburtstag'})
        form.fields['bemerkung'].widget = forms.Textarea(attrs={'cols' :5, 'rows': 2,
                                                                   'class': 'form-control'})
        return form


class TrainerAktualisieren(UpdateView):

    model = Trainer
    fields = [   'nachname', 'vorname', 'geb_datum', 'strasse',
                'hausnummer', 'plz', 'stadt',
                'festnetz', 'e_mail',
                'bemerkung'
             ]
    template_name_suffix = '_aktualisieren_form'
    success_url = reverse_lazy('trainer_liste')

    class Meta:
        pass

    def get_form(self, form_class=None):
        form = super(TrainerAktualisieren, self).get_form(form_class)
        form.fields['geb_datum'].widget = forms.DateInput(format=('%d.%m.%Y'),
                                                            attrs={'id':'datepicker-geburtstag',})
        form.fields['bemerkung'].widget = forms.Textarea(attrs={'cols' :5, 'rows': 2,
                                                                   'class': 'form-control'})
        return form


class TrainerEntfernen(DeleteView):
    model = Trainer
    success_url = reverse_lazy('trainer_liste')



## Zertfifizierungen views
def zertifizierung_liste(request):

    return render(request, 'kursverwaltung/zertifizierung-liste.html')



## Kurs Views

def kurs_liste(request):
    kurs_liste = Kurs.objects.order_by('id')
    context = {'kurs_liste':kurs_liste}
    return render(request, 'kursverwaltung/kurs-liste.html',context)


class KursErstellen(CreateView):
    template_name = "kurs_create_form.html"
    model = Kurs

    fields = [  'titel', 'anfangszeit', 'endzeit',
                'raum', 'trainer', 'max_teilnehmer',
                'gebuehr', 'beschreibung'
             ]
    success_url = reverse_lazy('kurs_liste')

    class Meta:
        pass

    def get_form(self, form_class=None):
        form = super(KursErstellen, self).get_form(form_class)
        form.fields['beschreibung'].required = False #später entfernen, soll True sein!
        form.fields['raum'].required = False #später entfernen, soll True sein!

        form.fields['anfangszeit'].widget = forms.DateInput(format=('%d.%m.%Y %H:%M'),
                                                            attrs={'id':'datetimepicker-anfangszeit'})
        form.fields['endzeit'].widget = forms.DateInput(format=('%d.%m.%Y %H:%M'),
                                                        attrs={'id':'datetimepicker-endzeit'})
        form.fields['beschreibung'].widget = forms.Textarea(attrs={'cols' :5, 'rows': 2,
                                                                   'class': 'form-control'})
        return form


class KursAktualisieren(UpdateView):

    model = Kurs
    fields = [  'titel', 'anfangszeit', 'endzeit',
                'raum', 'trainer', 'max_teilnehmer',
                'gebuehr', 'beschreibung'
             ]

    template_name_suffix = '_aktualisieren_form'
    success_url = reverse_lazy('kurs_liste')

    class Meta:
        pass

    def get_form(self, form_class=None):
        form = super(KursAktualisieren, self).get_form(form_class)
        form.fields['beschreibung'].required = False #später entfernen, soll True sein!
        form.fields['raum'].required = False #später entfernen, soll True sein!
        #form.fields['beschreibung'].required = False
        form.fields['anfangszeit'].widget = forms.DateInput(format=('%d.%m.%Y %H:%M'),
                                                            attrs={'id':'datetimepicker-anfangszeit'})
        form.fields['endzeit'].widget = forms.DateInput(format=('%d.%m.%Y %H:%M'),
                                                        attrs={'id':'datetimepicker-endzeit'})
        form.fields['beschreibung'].widget = forms.Textarea(attrs={'cols' :5, 'rows': 2,
                                                                   'class': 'form-control'})
        return form

class KursDetails(DetailView):

    model = Kurs
    template_name_suffix = '_details_form'

    class Meta:
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class KursEntfernen(DeleteView):
    model = Kurs
    success_url = reverse_lazy('kurs_liste')

    class Meta:
        pass

## Buchungen views
"""
def buchung_liste(request):

    return render(request, 'kursverwaltung/buchungen-liste.html')
"""

def buchungen_liste(request):
    buchungen_liste = Buchung.objects.order_by('id')
    context = {'buchungen_liste':buchungen_liste}
    trainer_liste = Trainer.objects.order_by('id')
    return render(request, 'kursverwaltung/buchungen-liste.html',
                  {'buchungen_liste':buchungen_liste, 'trainer_liste':trainer_liste})

class BuchungErstellen(CreateView):
    template_name = "buchung_create_form.html"
    model = Buchung

    fields = [ 'kurs_nr', 'kunde' ]

    success_url = reverse_lazy('buchungen_liste')

    def get_form(self, form_class=None):
        form = super(BuchungErstellen, self).get_form(form_class)
        # teilnehmerzahl soll automatisch ermittelt und aktualisert werden
        # feld darf dann nicht verändert werrden
        #form.fields['teilnehmerzahl'].required = False
        return form

    class Meta:
        pass

class BuchungAktualisieren(UpdateView):

    model = Buchung
    fields = [ 'kurs_nr', 'kunde' ]

    template_name_suffix = '_aktualisieren_form'
    success_url = reverse_lazy('buchungen_liste')

    def get_form(self, form_class=None):
        form = super(BuchungAktualisieren, self).get_form(form_class)
        # teilnehmerzahl soll automatisch ermittelt und aktualisert werden
        # feld darf dann nicht verändert werrden
        #form.fields['teilnehmerzahl'].required = False
        return form

    class Meta:
        pass

class BuchungEntfernen(DeleteView):
    model = Buchung
    success_url = reverse_lazy('buchungen_liste')

    class Meta:
        pass


## Räume views
def raum_liste(request):
    raum_liste = Raum.objects.order_by('id')
    context = {'raum_liste':raum_liste}
    return render(request, 'kursverwaltung/raum-liste.html',context)


class RaumErstellen(CreateView):
    template_name = "raum_create_form.html"
    model = Raum

    fields = [  'gebaeude', 'strasse','hausnummer', 'raum_nr',
                'plz', 'stadt', 'bemerkung',
                'sitzplaetze','ansprechpartner', 'geraeteverantwortlicher',

             ]
    success_url = reverse_lazy('raum_liste')

    class Meta:
        pass


    def get_form(self, form_class=None):
        form = super(RaumErstellen, self).get_form(form_class)
        form.fields['bemerkung'].required = False
        form.fields['bemerkung'].widget = forms.Textarea(attrs={'cols' :5, 'rows': 2,
                                                                'class': 'form-control'})
        """
        form.fields['ansprechpartner'].widget = forms.Textarea(attrs={'cols' :5, 'rows': 2,
                                                                              'class': 'form-control'})
        form.fields['geraeteverantwortlicher'].widget = forms.Textarea(attrs={'cols' :5, 'rows': 2,
                                                                              'class': 'form-control'})
        """
        return form

class RaumAktualisieren(UpdateView):

    model = Raum
    fields = [  'gebaeude', 'strasse','hausnummer', 'raum_nr',
                'plz', 'stadt', 'bemerkung',
                'sitzplaetze','ansprechpartner', 'geraeteverantwortlicher',

             ]

    template_name_suffix = '_aktualisieren_form'
    success_url = reverse_lazy('raum_liste')

    class Meta:
        pass

    def get_form(self, form_class=None):
        form = super(RaumAktualisieren, self).get_form(form_class)
        form.fields['bemerkung'].required = False
        form.fields['bemerkung'].widget = forms.Textarea(attrs={'cols' :5, 'rows': 2,
                                                                'class': 'form-control'})
        """
        form.fields['ansprechpartner'].widget = forms.Textarea(attrs={'cols' :5, 'rows': 2,
                                                                              'class': 'form-control'})
        form.fields['geraeteverantwortlicher'].widget = forms.Textarea(attrs={'cols' :5, 'rows': 2,
                                                                              'class': 'form-control'})
        """
        #form.fields['feld2'].required = False
        return form


class RaumEntfernen(DeleteView):
    model = Raum
    success_url = reverse_lazy('raum_liste')

## Zertifizierung views
def zertifizierungen_liste(request):
    zertifizierung_liste = Zertifizierung.objects.order_by('id')
    context = {'zertifizierung_liste':zertifizierung_liste}
    return render(request, 'kursverwaltung/zertifizierung-liste.html',context)


class ZertifizierungErstellen(CreateView):
    template_name = "zertifizierung_create_form.html"
    model = Zertifizierung

    fields = [  'name', 'trainer', 'gueltig_bis']
    success_url = reverse_lazy('zertifizierungen_liste')

    class Meta:
        pass

    def get_form(self, form_class=None):
        form = super(ZertifizierungErstellen, self).get_form(form_class)
        form.fields['gueltig_bis'].widget = forms.DateInput(format=('%d.%m.%Y'),
                                                        attrs={'id':'datepicker-zertifizierung'})
        return form

class ZertifizierungAktualisieren(UpdateView):

    model = Zertifizierung
    fields = [  'name', 'trainer', 'gueltig_bis']

    template_name_suffix = '_aktualisieren_form'
    success_url = reverse_lazy('zertifizierungen_liste')

    class Meta:
        pass

    def get_form(self, form_class=None):
        form = super(ZertifizierungAktualisieren, self).get_form(form_class)
        form.fields['gueltig_bis'].widget = forms.DateInput(format=('%d.%m.%Y'),
                                                        attrs={'id':'datepicker-zertifizierung'})
        return form


class ZertifizierungEntfernen(DeleteView):
    model = Zertifizierung
    success_url = reverse_lazy('zertifizierungen_liste')

    class Meta:
        pass
