from django.shortcuts import render
from .models import Signos
from django import forms

# Create your views here.
def MainPage(request):
    return render(request, 'MainPage.html', {})

def Contato(request):
    return render(request, 'App/Contato.html', {})

def MostrarTodosSelect(request, signo):
    select = True
    signos = Signos.objects.order_by('id')
    return render(request, 'App/TodosSignos.html', {'sign2' : signo, 'signos' : signos, 'select' : select})


def MostrarTodos(request):
    select = False
    signos = Signos.objects.order_by('id')
    return render(request, 'App/TodosSignos.html', {'signos' : signos})
    

def DescobrirSigno(request):
    if request.method == 'POST':
        dia = request.POST.get('dia')
        mes = request.POST.get('mes')
        dia2 = int(dia)
        mes2 = int(mes)
        if mes2 == 1:
            if dia2 <= 20:
                return MostrarTodosSelect(request, "Capricórnio")
            else:
                return MostrarTodosSelect(request, "Aquário")
        elif mes2 == 2:
            if dia2 <= 19:
                return MostrarTodosSelect(request, "Aquário")
            else:
                return MostrarTodosSelect(request, "Peixes")
        elif mes2 == 3:
            if dia2 <= 20:
                return MostrarTodosSelect(request, "Peixes")
            else:
                return MostrarTodosSelect(request, "Áries")
        elif mes2 == 4:
            if dia2 <= 20:
                return MostrarTodosSelect(request, "Áries")
            else:
                return MostrarTodosSelect(request, "Touro")
        elif mes2 == 5:
            if dia2 <= 20:
                return MostrarTodosSelect(request, "Touro")
            else:
                return MostrarTodosSelect(request, "Gêmeos")
        elif mes2 == 6:
            if dia2 <= 20:
                return MostrarTodosSelect(request, "Gêmeos")
            else:
                return MostrarTodosSelect(request, "Câncer")
        elif mes2 == 7:
            if dia2 <= 21:
                return MostrarTodosSelect(request, "Câncer")
            else:
                return MostrarTodosSelect(request, "Leão")
        elif mes2 == 8:
            if dia2 <= 22:
                return MostrarTodosSelect(request, "Leão")
            else:
                return MostrarTodosSelect(request, "Virgem")
        elif mes2 == 9:
            if dia2 <= 22:
                return MostrarTodosSelect(request, "Virgem")
            else:
                return MostrarTodosSelect(request, "Libra")
        elif mes2 == 10:
            if dia2 <= 22:
                return MostrarTodosSelect(request, "Libra")
            else:
                return MostrarTodosSelect(request, "Escorpião")
        elif mes2 == 11:
            if dia2 <= 21:
                return MostrarTodosSelect(request, "Escorpião")
            else:
                return MostrarTodosSelect(request, "Sagitário")
        else:
            if dia2 <= 21:
                return MostrarTodosSelect(request, "Sagitário")
            else:
                return MostrarTodosSelect(request, "Capricórnio")
    return render(request, 'App/DescobrirSigno.html', {})
