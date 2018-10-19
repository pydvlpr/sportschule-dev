from django.urls import path, re_path
from . import views

urlpatterns = [
    # index-Page
    path('',views.index, name='index'),

    # Kurs-Liste
    path('kurse/',views.kurs_liste, name='kurs_liste'),
    path('trainer/',views.trainer_liste, name='trainer_liste'),

]
