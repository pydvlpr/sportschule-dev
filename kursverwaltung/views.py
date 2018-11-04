from django.shortcuts import get_object_or_404,render, redirect
from django.urls import reverse_lazy, reverse
from django import forms
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

# Datum und Zeit
from datetime import datetime
from pytz import timezone


# Modelle
from .models.kunde import Kunde
from .models.trainer import Trainer
from .models.kurs import Kurs
from .models.raum import Raum
from .models.buchung import Buchung
from .models.zertifizierung import Zertifizierung

# Forms
from .forms import BuchungForm, KursForm

# eigene Funktionen
from .utils import time_in_range

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


class KundeDetails(DetailView):

    model = Kunde
    template_name_suffix = '_details_form'

    class Meta:
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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


class TrainerDetails(DetailView):

    model = Trainer
    template_name_suffix = '_details_form'

    class Meta:
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TrainerEntfernen(DeleteView):
    model = Trainer
    success_url = reverse_lazy('trainer_liste')


## Kurs Views

def kurs_liste(request):
    kurs_liste = Kurs.objects.order_by('id')
    context = {'kurs_liste':kurs_liste}
    return render(request, 'kursverwaltung/kurs-liste.html',context)


def kurs_erstellen(request):
    args = {}
    if request.method == "POST":
        form = KursForm(request.POST)
        if form.is_valid():
            # kursdaten übernehmen aus form quatsch, neuer_kurs = string des forms
            neuer_kurs = form.save(commit=False)

            # erforderliche Daten des neuen Kurses entnehmen
            neuer_kurs_anfangszeit = neuer_kurs.anfangszeit.astimezone(timezone('Europe/Berlin'))
            neuer_kurs_endzeit = neuer_kurs.endzeit.astimezone(timezone('Europe/Berlin'))
            neuer_kurs_tag = neuer_kurs_anfangszeit.date()

            # Form Daten für Kurs-Validierung
            neuer_kurs_raum = form.cleaned_data['raum']
            neuer_kurs_trainer = form.cleaned_data['trainer']

            # alle Kurs-Objekte der DB
            alle_kurse = Kurs.objects.all()
            # alle Kurse am selben Tag
            problem_kurse = []

            # Kurse durchlaufen
            for kurs in alle_kurse:
                #kurszeit auf localtime setzen
                kurs_beginn = kurs.anfangszeit.astimezone(timezone('Europe/Berlin'))
                kurs_beginn_tag = kurs.anfangszeit.astimezone(timezone('Europe/Berlin')).date()

                if neuer_kurs_tag == kurs_beginn_tag:
                    # Kurse am gleichen Tag sammeln für nachfolgende Prüfung
                    problem_kurse.append(kurs)


            # Kurse mit gleichem Tag prüfen
            for problem_kurs in problem_kurse:

                problem_kurs_beginn = problem_kurs.anfangszeit.astimezone(timezone('Europe/Berlin'))
                problem_kurs_ende = problem_kurs.endzeit.astimezone(timezone('Europe/Berlin'))
                problem_kurs_id = problem_kurs.id

                # zeitliche Überschneidungen prüfen
                # time_in_range(zeitraum_start, zeitraum_ende, zeitpunkt)
                if  time_in_range(problem_kurs_beginn, problem_kurs_ende, neuer_kurs_anfangszeit) or \
                    time_in_range(problem_kurs_beginn, problem_kurs_ende, neuer_kurs_endzeit) or \
                    time_in_range(problem_kurs_beginn, problem_kurs_ende, neuer_kurs_anfangszeit) and \
                    time_in_range(problem_kurs_beginn, problem_kurs_ende, neuer_kurs_endzeit) or \
                    time_in_range(neuer_kurs_anfangszeit, neuer_kurs_endzeit, problem_kurs_beginn) or \
                    time_in_range(neuer_kurs_anfangszeit, neuer_kurs_endzeit, problem_kurs_beginn) and \
                    time_in_range(neuer_kurs_anfangszeit, neuer_kurs_endzeit, problem_kurs_ende):


                    # Raum Doppelbelegung prüfen
                    problem_kurs_raum = problem_kurs.raum
                    if problem_kurs_raum == neuer_kurs_raum:
                        raum_dummy = "in if raum..."
                        raum_object = get_object_or_404(Raum, pk=neuer_kurs_raum.id)
                        kurs_object = get_object_or_404(Kurs, pk=problem_kurs.id)
                        error_message = "Der Raum ist bereits belegt."

                        ##DEBUG
                        #balfa = Kurs.objects.by_id("200")

                        return render(request, 'kursverwaltung/kurs_validieren_error.html',
                                      {'error_message':error_message, 'raum_object':raum_object, 'kurs_object':kurs_object})


                    # Trainer Doppelbuchung prüfen
                    problem_kurs_trainer = problem_kurs.trainer
                    if problem_kurs_trainer  == neuer_kurs_trainer:
                        trainer_dummy = "in if trainer..."
                        trainer_object = get_object_or_404(Trainer, pk=problem_kurs_trainer.id)
                        kurs_object = get_object_or_404(Kurs, pk=problem_kurs.id)
                        error_message = "Der Trainer ist bereits gebucht."

                        ##DEBUG
                        #balfa = Kurs.objects.by_id("200")

                        return render(request, 'kursverwaltung/kurs_validieren_error.html',
                                      {'error_message':error_message, 'trainer_object':trainer_object, 'kurs_object':kurs_object})

                # greift, wenn Zeitfilter, d.h. Kurs wurde negativ geprüft
                else:
                    # Prüfung mit nächstem Kurs fortsetzen
                    continue

            # Neuen Kurs in DB speichern, wenn alles ok
            neuer_kurs.save()
            return redirect('kurs_liste')
        else:
            # Fehler bei fehlgeschlagener Validierung des Forms
            error_message = "Ein Fehler bei der Form-Verarbeitung ist aufgetreten"
            return render(request, 'kursverwaltung/kurs_validieren_error.html',
                          {'error_message':error_message})
    else:
        form = KursForm()

    args['form']=form
    return render(request, "kursverwaltung/kurs_create_form.html", args)


def kurs_aktualisieren(request, pk):
    args = {}
    kurs = get_object_or_404(Kurs, pk=pk)
    if request.method == "POST":
        form = KursForm(request.POST, instance=kurs)
        if form.is_valid():
            # kursdaten übernehmen aus form quatsch, neuer_kurs = string des forms
            neuer_kurs = form.save(commit=False)

            # erforderliche Daten des neuen Kurses entnehmen
            neuer_kurs_anfangszeit = neuer_kurs.anfangszeit.astimezone(timezone('Europe/Berlin'))
            neuer_kurs_endzeit = neuer_kurs.endzeit.astimezone(timezone('Europe/Berlin'))
            neuer_kurs_tag = neuer_kurs_anfangszeit.date()

            # Form Daten für Kurs-Validierung
            neuer_kurs_raum = form.cleaned_data['raum']
            neuer_kurs_trainer = form.cleaned_data['trainer']

            # alle Kurs-Objekte der DB
            alle_kurse = Kurs.objects.all()
            # alle Kurse am selben Tag
            problem_kurse = []


            #blafa=Kurs.objects.by_id(200)

            # Kurse durchlaufen
            for kurs in alle_kurse:
                if kurs.id == neuer_kurs.id:
                    continue
                #kurszeit auf localtime setzen
                kurs_beginn = kurs.anfangszeit.astimezone(timezone('Europe/Berlin'))
                kurs_beginn_tag = kurs.anfangszeit.astimezone(timezone('Europe/Berlin')).date()

                if neuer_kurs_tag == kurs_beginn_tag:
                    # Kurse am gleichen Tag sammeln für nachfolgende Prüfung
                    problem_kurse.append(kurs)


            # Kurse mit gleichem Tag prüfen
            for problem_kurs in problem_kurse:

                problem_kurs_beginn = problem_kurs.anfangszeit.astimezone(timezone('Europe/Berlin'))
                problem_kurs_ende = problem_kurs.endzeit.astimezone(timezone('Europe/Berlin'))
                problem_kurs_id = problem_kurs.id

                # zeitliche Überschneidungen prüfen
                # time_in_range(zeitraum_start, zeitraum_ende, zeitpunkt)
                if  time_in_range(problem_kurs_beginn, problem_kurs_ende, neuer_kurs_anfangszeit) or \
                    time_in_range(problem_kurs_beginn, problem_kurs_ende, neuer_kurs_endzeit) or \
                    time_in_range(problem_kurs_beginn, problem_kurs_ende, neuer_kurs_anfangszeit) and \
                    time_in_range(problem_kurs_beginn, problem_kurs_ende, neuer_kurs_endzeit) or \
                    time_in_range(neuer_kurs_anfangszeit, neuer_kurs_endzeit, problem_kurs_beginn) or \
                    time_in_range(neuer_kurs_anfangszeit, neuer_kurs_endzeit, problem_kurs_beginn) and \
                    time_in_range(neuer_kurs_anfangszeit, neuer_kurs_endzeit, problem_kurs_ende):


                    # Raum Doppelbelegung prüfen
                    problem_kurs_raum = problem_kurs.raum
                    if problem_kurs_raum == neuer_kurs_raum:
                        raum_dummy = "in if raum..."
                        raum_object = get_object_or_404(Raum, pk=neuer_kurs_raum.id)
                        kurs_object = get_object_or_404(Kurs, pk=problem_kurs.id)
                        error_message = "Der Raum ist bereits belegt."

                        ##DEBUG
                        #balfa = Kurs.objects.by_id("200")

                        return render(request, 'kursverwaltung/kurs_validieren_error.html',
                                      {'error_message':error_message, 'raum_object':raum_object, 'kurs_object':kurs_object})


                    # Trainer Doppelbuchung prüfen
                    problem_kurs_trainer = problem_kurs.trainer
                    if problem_kurs_trainer  == neuer_kurs_trainer:
                        trainer_dummy = "in if trainer..."
                        trainer_object = get_object_or_404(Trainer, pk=problem_kurs_trainer.id)
                        kurs_object = get_object_or_404(Kurs, pk=problem_kurs.id)
                        error_message = "Der Trainer ist bereits gebucht."

                        ##DEBUG
                        #balfa = Kurs.objects.by_id("200")

                        return render(request, 'kursverwaltung/kurs_validieren_error.html',
                                      {'error_message':error_message, 'trainer_object':trainer_object, 'kurs_object':kurs_object})

                # greift, wenn Zeitfilter, d.h. Kurs wurde negativ geprüft
                else:
                    # Prüfung mit nächstem Kurs fortsetzen
                    continue

            # Neuen Kurs in DB speichern, wenn alles ok
            neuer_kurs.save()
            return redirect('kurs_liste')
        else:
            # Fehler bei fehlgeschlagener Validierung des Forms
            error_message = "Ein Fehler bei der Form-Verarbeitung ist aufgetreten"
            return render(request, 'kursverwaltung/kurs_validieren_error.html',
                          {'error_message':error_message})
    else:
        form = KursForm(instance=kurs)

    args['form']=form
    return render(request, "kursverwaltung/kurs_aktualisieren_form.html", args)

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

def buchungen_liste(request):
    buchungen_liste = Buchung.objects.order_by('id')
    context = {'buchungen_liste':buchungen_liste}
    trainer_liste = Trainer.objects.order_by('id')

    return render(request, 'kursverwaltung/buchungen-liste.html',
                  {'buchungen_liste':buchungen_liste, 'trainer_liste':trainer_liste})


"""
 Buchung erstellen mit eigenem Form für mehr Möglichkeiten
 zur Validierung der Teilnehmerzahl
"""
def buchung_erstellen(request):
    args = {}
    if request.method == "POST":
        form = BuchungForm(request.POST)
        if form.is_valid():
            # uncleand kurs enthält die gewählte Kurs.id
            kurs_id = request.POST['kurs']
            kurs = Kurs.objects.get(pk=kurs_id)
            kursbuchungen = Buchung.objects.filter(kurs=kurs_id).count()

            max = kurs.max_teilnehmer
            aktuelle_teilnehmerzahl = kurs.teilnehmerzahl

            # Validierung der Teilnehmerzahl
            if aktuelle_teilnehmerzahl < max:
                kurs.teilnehmerzahl = kursbuchungen+1
                # neue teilnehmerzahl speichern
                kurs.save()
                # buchung form speichern
                post = form.save()
                post.save()
                return redirect('buchungen_liste')
            else:
                # Fehler bei fehlgeschlagener Validierung
                error_message = "Der Kurs ist schon voll ( "+str(kursbuchungen)+" Teilnehmer)"
                return render(request, 'kursverwaltung/buchung_validieren_error.html',
                              {'error_message':error_message})
    else:
        form = BuchungForm()

    args['form']=form
    return render(request, "kursverwaltung/buchung_create_form.html", args)


"""
 Buchung erstellen mit eigenem Form für mehr Möglichkeiten
 zur Validierung der teilnehmerzahl
"""
def buchung_aktualisieren(request,pk):
    args = {}
    buchung = get_object_or_404(Buchung, pk=pk)
    if request.method == "POST":
        form = BuchungForm(request.POST, instance = buchung)
        if form.is_valid():
            # uncleand kurs enthält die gewählte Kurs.id
            kurs_id = request.POST['kurs']
            # Kurs Objekte zur ID  holen und zählen
            kurs = Kurs.objects.get(pk=kurs_id)
            kursbuchungen = Buchung.objects.filter(kurs=kurs_id).count()

            max = kurs.max_teilnehmer
            aktuelle_teilnehmerzahl = kurs.teilnehmerzahl

            # Validierung der Teilnehmerzahl
            if aktuelle_teilnehmerzahl < max:
                kurs.teilnehmerzahl = kursbuchungen+1
                # neue teilnehmerzahl speichern
                kurs.save()
                # buchung form speichern
                post = form.save()
                post.save()
                return redirect('buchungen_liste')
            else:
                # Fehler bei fehlgeschlagener Validierung
                error_message = "Der Kurs ist schon voll ( "+str(kursbuchungen)+" Teilnehmer)"
                return render(request, 'kursverwaltung/buchung_validieren_error.html',
                              {'error_message':error_message})
    else:
        form = BuchungForm(instance=buchung)

    args['form']=form
    return render(request, "kursverwaltung/buchung_aktualisieren_form.html", args)


# Reduzierung der Teilnehmerzahl bei Löschung noch implementieren
def buchung_entfernen(request,pk):
    buchung = get_object_or_404(Buchung, pk=pk)
    if request.method == "POST":
        kurs = get_object_or_404(Kurs, pk=buchung.kurs.id)

        aktuelle_teilnehmerzahl = kurs.teilnehmerzahl

        # Validierung der Teilnehmerzahl
        if aktuelle_teilnehmerzahl >= 0:
            # neue teilnehmerzahl festlegen und speichern
            kurs.teilnehmerzahl= aktuelle_teilnehmerzahl - 1
            kurs.save()

            # Buchung Löschen
            buchung.delete()
            return redirect ('buchungen_liste')

        else:
            # Fehler bei fehlgeschlagener Validierung
            error_message = "Es sind keine Teilnehmer mehr vorhanden."
            return render(request, 'kursverwaltung/buchung_validieren_error.html',
                          {'error_message':error_message})

    return render(request, "kursverwaltung/buchung_confirm_delete.html", {"object":buchung})


"""
 Räume views
"""

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
        form.fields['geraeteverantwortlicher'].required = False
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
        form.fields['geraeteverantwortlicher'].required = False
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
        form.fields['name'].widget = forms.TextInput(attrs={'class':'has-popover',
                                                             'data-content':"Name der Zertifizierung eingeben.",
                                                             'data-placement':'right',
                                                             'data-container':'body'})

        form.fields['gueltig_bis'].widget = forms.DateInput(format=('%d.%m.%Y'),
                                                        attrs={'id':'datepicker-zertifizierung',
                                                               'class':'has-popover',
                                                               'data-content':"Gültigkeitsdatum der Zertifizierung eingeben.",
                                                               'data-placement':'right',
                                                               'data-container':'body'})

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
        form.fields['name'].widget = forms.TextInput(attrs={'class':'has-popover',
                                                             'data-content':"Name der Zertifizierung eingeben.",
                                                             'data-placement':'right',
                                                             'data-container':'body'})

        form.fields['gueltig_bis'].widget = forms.DateInput(format=('%d.%m.%Y'),
                                                        attrs={'id':'datepicker-zertifizierung',
                                                               'class':'has-popover',
                                                               'data-content':"Gültigkeitsdatum der Zertifizierung eingeben.",
                                                               'data-placement':'right',
                                                               'data-container':'body'})
        return form


class ZertifizierungEntfernen(DeleteView):
    model = Zertifizierung
    success_url = reverse_lazy('zertifizierungen_liste')

    class Meta:
        pass


def trainer_suchen(request):
    """
    Einfacher View für Suche
    """

    query = request.GET['q']
    search_tag = "SUCHE"

    if query != "":
        # zerfizierungen durchsuchen und relvante Trainer (Objekte) in Liste sammeln
        zertifizierungen_liste = Zertifizierung.objects.filter(name__contains=query)
        trainer_liste = []
        for zertifzierung in zertifizierungen_liste:
            trainer_liste.append(Trainer.objects.get(id=zertifzierung.trainer.id))

    else:
        # alle Trainer zurückgeben, wenn nichts gefunden wird
        zertifizierungen_liste = Zertifizierung.objects.all()
        trainer_liste = Trainer.objects.all()

    return render(request, "kursverwaltung/trainer-liste.html",
            {"trainer_liste": trainer_liste, "zertifizierungen_liste":zertifizierungen_liste, "search_tag":search_tag})
