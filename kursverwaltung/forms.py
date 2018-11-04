from django import forms
from django.urls import reverse_lazy

from .models.buchung import Buchung
from .models.kurs import Kurs


class BuchungForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BuchungForm,self).__init__(*args, **kwargs)
        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                self.fields[field].widget.attrs.update(
                    {'class':'has-popover', 'data-content':help_text, 'data-placement':'right', 'data-container':'body'})

    class Meta:
        model = Buchung
        fields = ( 'kurs', 'kunde' )


class KursForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(KursForm,self).__init__(*args, **kwargs)
        self.fields['beschreibung'].required = True
        self.fields['raum'].required = False
        self.fields['teilnehmerzahl'].disabled=True
        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                self.fields[field].widget.attrs.update(
                    {'class':'has-popover', 'data-content':help_text, 'data-placement':'right', 'data-container':'body'})


    class Meta:
        template_name = "kurs_create_form.html"
        model = Kurs

        fields = (  'titel', 'anfangszeit', 'endzeit',
                    'raum', 'trainer', 'max_teilnehmer', 'teilnehmerzahl',
                    'gebuehr', 'beschreibung'
                 )
        success_url = reverse_lazy('kurs_liste')
        pass

        widgets = {
            'anfangszeit': forms.DateInput(format=('%d.%m.%Y %H:%M'),
                                            attrs={'id':'datetimepicker-anfangszeit'}),
            'endzeit': forms.DateInput(format=('%d.%m.%Y %H:%M'),
                                        attrs={'id':'datetimepicker-endzeit'}),
            'beschreibung': forms.Textarea(attrs={'cols' :20, 'rows': 2}),
        }

    def get_form(self, form_class=None):
        form = super(KursErstellen, self).get_form(form_class)
        form.fields['beschreibung'].required = False #später entfernen, soll True sein!
        form.fields['raum'].required = False #später entfernen, soll True sein!
        form.fields['teilnehmerzahl'].disabled=True

        form.fields['anfangszeit'].widget = forms.DateInput(format=('%d.%m.%Y %H:%M'),
                                                            attrs={'id':'datetimepicker-anfangszeit'})
        form.fields['endzeit'].widget = forms.DateInput(format=('%d.%m.%Y %H:%M'),
                                                        attrs={'id':'datetimepicker-endzeit'})
        form.fields['beschreibung'].widget = forms.Textarea(attrs={'cols' :5, 'rows': 2,
                                                                   'class': 'form-control'})
        return form
