from django.shortcuts import render, redirect
from .models import Posts

def index(request):
    if request.method == 'POST':
        # Recuperar os dados do formulário
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        imagem = request.FILES.get('imagem')

        # Validar e salvar os dados no banco de dados
        if titulo and descricao:
            post = Posts(titulo=titulo, descricao=descricao, imagem=imagem)
            post.save()
            return redirect('index')  # Redireciona após salvar

    return render(request, 'index.html')
