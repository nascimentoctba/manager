from django.shortcuts import render
#from blog.data import posts
import requests 


def blog(request):
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
    else:
        posts = {'error_message':'Erro na solicitação'}

    context ={
        'titulo':'Pagina Inicial do Blog',
        'title_page':'Manager Tex - Blog',
        'posts':posts
    }
    return render(
        request, 
        'blog/index.html',
        context,
    )


def exemplo(request):
    context ={
        'titulo':'Pagina inicial do Exemplo',
        'title_page':'Manager Tex - Exemplo'
    }
    return render(
        request,
        'blog/exemplo.html',
        context,
    )


def vendas(request):
    context ={
        'titulo':'Pagina inicial de Vendas',
        'title_page':'Manager Tex - Vendas'
    }
    return render(
        request,
        'blog/vendas.html',
        context,
    )

