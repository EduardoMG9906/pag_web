from django.shortcuts import render
from django.http import HttpResponse
from .models import participantes
# Create your views here.

def inicio(request):
    return render(request, 'paginas/index.html')

def list_participantes(request):
    participante = participantes.objects.all()
    hym = participante.count
    mujeres = participante.filter(genero='Femenino').count()
    hombres = participante.filter(genero='Masculino').count()
    
    
    filtro_cedula = request.GET.get('filtro_cedula', '')  # Obtenemos el valor del parámetro o '' si no existe
    
    if filtro_cedula: 
        participante = participante.filter(cedula=filtro_cedula) 
        
    return render(request, 'Participantes/Listar.html', {
        'participantes': participante,
        'mujeres': mujeres,
        'hombres': hombres,
        'hym': hym
        })