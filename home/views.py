from django.shortcuts import render

def home(request):
    print('Home1')
    
    context = {
        'titulo':'Estamos na pagina Home',
        'title_page':'Manager Tex'
    }
    

    return render(     
        request,
        'home/index.html', 
        context,
    )

