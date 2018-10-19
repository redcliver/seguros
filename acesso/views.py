from django.shortcuts import render
from deltatres.models import cliente
# Create your views here.
def acesso(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'deltatres':
            clientes = cliente.objects.all().order_by('nome')
            return render(request, 'deltatres/home_delta.html', {'title':'Home','clientes':clientes})
        elif empresa == 'headtec':
            return render(request, 'home/home.html', {'title':'Home'})
        return render(request, 'home/erro.html', {'title':'Erro'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})