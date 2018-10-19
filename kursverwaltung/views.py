from django.shortcuts import get_object_or_404,render, redirect

# Index-Site
def index(request):
    return render(request, 'kursverwaltung/index.html')

def kurs_liste(request):
    #kurs_liste = Kurse.objects.order_by('id')
    #context = {'kurs_liste':course_list}
    #return render(request, 'kursverwaltung/kurs-liste.html',context)
    return render(request, 'kursverwaltung/kurs-liste.html')

def trainer_liste(request):
    #kurs_liste = Kurse.objects.order_by('id')
    #context = {'kurs_liste':course_list}
    #return render(request, 'kursverwaltung/kurs-liste.html',context)
    return render(request, 'kursverwaltung/trainer-liste.html')
