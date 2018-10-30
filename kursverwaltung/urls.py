from django.urls import path, re_path, reverse
from . import views

urlpatterns = [
    # index-Page
    path('',views.kurs_liste, name='index'),

    # Kurs-Liste
    path('kurse/',views.kurs_liste, name='kurs_liste'),

    #urls für Übersichten
    path('trainer/',views.trainer_liste, name='trainer_liste'),
    path('kunden/',views.kunden_liste, name='kunden_liste'),
    path('buchungen/',views.buchungen_liste, name='buchungen_liste'),
    path('raum/',views.raum_liste, name='raum_liste'),
    path('zertifizierungen/',views.zertifizierungen_liste, name='zertifizierungen_liste'),

    # urls Kunden Formulare
    path('kunden/neu/', views.KundeErstellen.as_view(), name='kunde_erstellen'),
    path('kunden/aktualisieren/<int:pk>/', views.KundeAktualisieren.as_view(), name='kunde_aktualisieren'),
    path('kunden/entfernen<int:pk>/', views.KundeEntfernen.as_view(), name='kunde_entfernen'),

    # urls Trainer Formulare
    path('trainer/neu/', views.TrainerErstellen.as_view(), name='trainer_erstellen'),
    path('trainer/aktualisieren/<int:pk>/', views.TrainerAktualisieren.as_view(), name='trainer_aktualisieren'),
    path('trainer/entfernen/<int:pk>/', views.TrainerEntfernen.as_view(), name='trainer_entfernen'),

    # urls Raum Formulare
    path('raum/neu/', views.RaumErstellen.as_view(), name='raum_erstellen'),
    path('raum/aktualisieren/<int:pk>/', views.RaumAktualisieren.as_view(), name='raum_aktualisieren'),
    path('raum/entfernen/<int:pk>/', views.RaumEntfernen.as_view(), name='raum_entfernen'),

    # urls Kurs Formulare
    path('kurse/neu/', views.KursErstellen.as_view(), name='kurs_erstellen'),
    path('kurse/<int:pk>/', views.KursDetails.as_view(), name='kurs_details'),
    path('kurse/aktualisieren/<int:pk>/', views.KursAktualisieren.as_view(), name='kurs_aktualisieren'),
    path('kurse/entfernen/<int:pk>/', views.KursEntfernen.as_view(), name='kurs_entfernen'),

    # urls Buchung Formulare
    path('buchungen/neu/', views.buchung_erstellen, name='buchung_erstellen'),
    path('buchungen/aktualisieren/<int:pk>/', views.buchung_aktualisieren, name='buchung_aktualisieren'),
    path('buchungen/entfernen/<int:pk>/', views.buchung_entfernen, name='buchung_entfernen'),

    # urls Zertifizierung Formulare
    path('zertifizierung/neu/', views.ZertifizierungErstellen.as_view(), name='zertifizierung_erstellen'),
    path('zertifizierung/aktualisieren/<int:pk>/', views.ZertifizierungAktualisieren.as_view(), name='zertifizierung_aktualisieren'),
    path('zertifizierung/entfernen/<int:pk>/', views.ZertifizierungEntfernen.as_view(), name='zertifizierung_entfernen'),
]
