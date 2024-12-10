from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import motorv8, motorv6, motori4  
from .forms import MotorV8Form,MotorI4Form,MotorV6Form

def inicio(request):
    return render(request, 'motor/index.html')

def vista_motor_v8(request):
    query = request.GET.get("q")
    if query:
        v8 = motorv8.objects.filter(marca__icontains=query)
    else:
        v8 = motorv8.objects.all()

    return render(request, "motor/listado_motoresv8.html",{"v8":v8})

def vista_motor_v6(request):
    return render(request, "motor/V6.html")

def vista_motor_i4(request):
    return render(request, "motor/I4.html")

def crear_motor_v8(request):
    if request.method == 'POST':
        form = MotorV8Form(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('inicio') 
    else:
        form = MotorV8Form() 
    
    return render(request, 'motor/form/crear_motorv8.html', {'form': form})

def crear_motor_v6(request):
    if request.method == 'POST':
        form = MotorV6Form(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('inicio') 
    else:
        form = MotorV8Form() 
    
    return render(request, 'motor/form/crear_motorv6.html', {'form': form})

def crear_motor_I4(request):
    if request.method == 'POST':
        form = MotorI4Form(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('inicio') 
    else:
        form = MotorV8Form() 
    
    return render(request, 'motor/form/crear_motori4.html', {'form': form})

def listado_motoresv8(request):
    
    motores_v8 = motorv8.objects.all()


    return render(request, 'motor/listado_motoresv8.html', {
        'motores_v8': motores_v8,
  })
def listado_motoresv6(request):

    motores_v6 = motorv6.objects.all()

    return render(request, 'motor/listado_motoresv6.html', {
        'motores_v6': motores_v6,

  })
def listado_motoresi4(request):
    motores_i4 = motori4.objects.all()

    return render(request, 'motor/listado_motoresi4.html', {
        'motores_i4': motores_i4
  })


def listado_motores(request):
    motores_v8 = motorv8.objects.all()
    motores_v6 = motorv6.objects.all()
    motores_i4 = motori4.objects.all()

    return render(request, 'motor/listado_motores.html', {
        'motores_v8': motores_v8,
        'motores_v6': motores_v6,
        'motores_i4': motores_i4
    })



