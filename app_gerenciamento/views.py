from django.shortcuts import render, get_object_or_404
from .models import Ordem_de_servico
# Create your views here.

def home(request):
    return render(request, 'home.html')

def servico(request):
    servicos = Ordem_de_servico.objects.all()
    return render(request, 'servico.html', {'servicos': servicos})

def registrar_os(request):
    if request.method == 'POST':
        os = request.POST.get('os')
        pa = request.POST.get('p_a')
        pc = request.POST.get('p_c')
        operacao = request.POST.get('operacao')
        n_operacao = request.POST.get('n_operacao')
        nome_pc = request.POST.get('nome_pc')
        endereco = request.POST.get('endereco')
        uo = request.POST.get('uo')
        fixacao = request.POST.get('fixacao')
        data = request.POST.get('data')
        hora = request.POST.get('hora')

        if Ordem_de_servico.objects.filter(os=os, p_c=pc).exists():
            return render(request, 'registro_os.html')
        else:
            Ordem_de_servico.objects.create(os=os, p_a=pa, p_c=pc, operacao=operacao, n_operacao=n_operacao,
                                            nome_pc=nome_pc, endereco=endereco, uo= uo, fixacao=fixacao,
                                            data=data, hora=hora)
            return render(request, 'registro_os.html', {'success': 'Registro criado com sucesso.'})
    else:
        return render(request, 'registro_os.html')


def info_os(request, slug):
    servico = get_object_or_404(Ordem_de_servico, slug=slug)
    return render(request, 'info_os.html', {'servico':servico})
    