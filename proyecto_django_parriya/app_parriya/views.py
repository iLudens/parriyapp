from django.shortcuts import render, redirect
from . forms import UsuarioForm, RecetaForm, ParrillerroForm, DispoForm, ResForm
from .models import Usuario, Recetas, Parrilleros, Disponibilidad, Reserva
from django.contrib.sessions.models import Session
import json
from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal
from .helpers import generate_slug


def inicio(request):

    if not 'usuario_autenticado' in request.session:

        if request.method == "POST":

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = Usuario.objects.filter(
                nombre_usuario=username, contrasena=password).exists()

            if user is not False:

                usuario = Usuario.objects.filter(
                    nombre_usuario=username, contrasena=password).values()

                request.session['usuario_autenticado'] = username
                usuario_serializable = [{k: (float(v) if isinstance(
                    v, Decimal) else v) for k, v in u.items()} for u in usuario]

                request.session['data'] = json.dumps(
                    usuario_serializable, cls=DjangoJSONEncoder)

                return redirect('pagina2')
            else:
                return render(request, 'inicio.html')

        elif request.method == "GET":
            return render(request, 'inicio.html')

    else:
        return redirect('pagina2')


def pagina1(request):
    return render(request, 'pagina1.html')


def pagina2(request):

    if not 'usuario_autenticado' in request.session:
        return redirect('inicio')

    return render(request, 'pagina2.html')


def formulario(request):
    if request.method == 'POST':
        try:
            form = UsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                # hacer algo después de guardar los datos del usuario
        except NameError as ex:
            print(ex)
    else:
        form = UsuarioForm()
    return render(request, 'formulario.html', {'form': form})


def logout(request):
    if not 'usuario_autenticado' in request.session:
        return redirect('inicio')

    request.session.flush()
    return redirect('inicio')


def views2(request):

    return render(request, 'page2.html')


def nosotros(request):
    return render(request, 'nosotros.html')


def servicios(request):
    return render(request, 'servicios.html')


def contactos(request):
    return render(request, 'contactos.html')


def recetas(request):

    if request.method == 'POST':
        try:
            form = RecetaForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('recetas')
            else:
                return redirect('recetas')
        except Exception as ex:
            print(ex)

    data_recetas = Recetas.objects.all()

    data = {
        'form': RecetaForm(),
        'data_recetas': data_recetas
    }

    return render(request, 'recetas.html', context=data)


def parrilleros(request):

    if request.method == 'POST':
        print("POST")
        form = ParrillerroForm(request.POST, request.FILES)
        print("Entrando")
        if form.is_valid():
            form.save()
            return redirect('parrilleros')
        else:
            return redirect('parrilleros')

    data = {
        'form_parrillero': ParrillerroForm()
    }
    return render(request, 'parrilleros.html', context=data)


def disponibilidad(request):
    form = DispoForm()
    if request.method == 'POST':
        form = DispoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = DispoForm()

    disponibles = Disponibilidad.objects.all()
    data = {'form': form, 'disponibles': disponibles}
    return render(request, 'disponibilidad.html', data)

def reserva(request):
    form = ResForm()
    if request.method == 'POST':
        form = ResForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
    
    reservas = Reserva.objects.all()
    data = {'form': form, 'reservas': reservas}
    return render(request, 'reserva.html', data)


def endpoint_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recetas')
    else:
        return render(request, 'parrilleros.html')

