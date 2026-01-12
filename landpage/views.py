# views
from django.shortcuts import render, redirect
from django.http import Http404

from .dados import projetos
from .forms import ContatoForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Enviar email
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            telefone = form.cleaned_data['telefone']
            mensagem = form.cleaned_data['mensagem']
            
            corpo_email = f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}  \nAssunto: {assunto}\nMensagem: {mensagem}"

            email = EmailMessage(
                subject=assunto,
                body=corpo_email,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[email]
            )
            email.send()
            messages.success(request, 'Email enviado com sucesso!')
            return redirect('home') 
    else:
        form = ContatoForm()
    return render(request, 'landpage/home.html', {'projetos': projetos, 'form':form})


def projetos_view(request):
    return render(request, 'landpage/projetos.html', {'projetos': projetos})


def detalhes_projetos(request, id_projeto):
    projeto = projetos.get(id_projeto)
    if projeto is None:
        raise Http404('Projeto não encontrado')
    return render(request, 'landpage/detalhes_projetos.html', {'projeto': projeto})
# def lista_projetos(request):