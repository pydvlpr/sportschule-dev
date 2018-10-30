from django import forms


from .models.buchung import Buchung


class BuchungForm(forms.ModelForm):

    class Meta:
        model = Buchung
        fields = ( 'kurs', 'kunde' )
