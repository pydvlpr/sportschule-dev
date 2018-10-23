from django.urls import path, re_path, reverse
from . import views

urlpatterns = [
    # index-Page
    path('',views.index, name='index'),

    # Kurs-Liste
    path('kurse/',views.kurs_liste, name='kurs_liste'),

    #urls für Übersichten
    path('trainer/',views.trainer_liste, name='trainer_liste'),
    path('kunden/',views.kunden_liste, name='kunden_liste'),
    path('buchungen/',views.buchungen_liste, name='buchungen_liste'),
    path('raeume/',views.raum_liste, name='raum_liste'),
    path('zertifizierungen/',views.zertifizierung_liste, name='zertifizierung_liste'),

    # urls Kunden Formulare
    path('kunden/add/', views.KundeErstellen.as_view(), name='kunde_erstellen'),
    path('kunden/<int:pk>/', views.KundeAktualisieren.as_view(), name='kunde_aktualisieren'),
    path('kunden/<int:pk>/entfernen/', views.KundeEntfernen.as_view(), name='kunde_entfernen'),

]
