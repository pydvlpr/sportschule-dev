from django.shortcuts import get_object_or_404,render, redirect

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
