from contextvars import Context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiares
from django.template import Template, Context
# Create your views here.

def familiar(request, edad, nombre, fecha_nacimiento):

    familiar = Familiares(edad=edad, nombre=nombre, fecha_nacimiento=fecha_nacimiento)
    familiar.save()

    return HttpResponse(f"<p>Edad: {familiar.edad} - Nombre: {familiar.nombre} - Fecha de nacimiento: {familiar.fecha_nacimiento} se agrego</p>")


def template(request):
    
    familiares = Familiares.objects.all()
    return render(request, "Template1.html", {"template": familiares})

