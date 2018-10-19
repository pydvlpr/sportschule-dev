from django.shortcuts import get_object_or_404,render, redirect

# Index-Site
def index(request):
    return render(request, 'kursverwaltung/index.html')
