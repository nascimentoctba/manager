from django.shortcuts import render

def blog(request):
    context ={
        'titulo':'Pagina Inicial do Blog',
        'title_page':'Manager Tex - Blog'
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

