from django.shortcuts import render
from .models import Ficha, Tarea
from .utils import average_rating

def index(request):
    return render(request,"base.html")


def ficha_list(request):
    fichas = Ficha.objects.all()
    ficha_list = []
    for ficha in fichas:
        fichaa = ficha.caratula
        if fichaa:
            number_of_tareas = len(fichaa)
        else:
            number_of_tareas = 0
        ficha_list.append({'ficha': ficha,\
                          'number_of_tareas': number_of_tareas})
    context = {
        'ficha_list': ficha_list
    }
    return render(request, 'fichas/ficha_list.html', context)

def casos_list(request):
    casos = Ficha.objects.all()
    casos_list = []
    for caso in casos:
        fichaa = caso.caratula
        if fichaa:
            number_de_tareas = len(fichaa)
        else:
            number_de_tareas = 0
        casos_list.append({'caso': caso,\
                          'number_de_tareas': number_de_tareas})
    context = {
        'casos_list': casos_list
    }
    return render(request, 'fichas/casos_list.html', context)