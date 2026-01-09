# views
from django.shortcuts import render
from django.http import Http404

from .dados import habilidades, projetos


def home(request):
    return render(request, 'landpage/home.html', {'habilidades': habilidades, 'projetos': projetos})


def projetos_view(request):
    return render(request, 'landpage/projetos.html', {'projetos': projetos})


def detalhes_projetos(request, id_projeto):
    projeto = projetos.get(id_projeto)
    if projeto is None:
        raise Http404('Projeto não encontrado')
    return render(request, 'landpage/detalhes_projetos.html', {'projeto': projeto})
# def lista_projetos(request):