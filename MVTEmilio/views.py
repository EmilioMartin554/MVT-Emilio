from django.shortcuts import render
from .models import Persona
from django.http import HttpResponse
from django.template import Context, loader 

def familiares(request):
    Madre=Persona(nombre="Liliana",edad=60,documento=13208339,fecha_nacimiento="24/8/1962",parentezco="Madre")
    Madre.save()
    Padre=Persona(nombre="Ernesto",edad=63,documento=13308723,fecha_nacimiento="24/8/1959",parentezco="Padre")
    Padre.save()
    Hermano=Persona(nombre="Emiliano",edad=29,documento=36779452,fecha_nacimiento="24/3/1993",parentezco="Hermano")
    Hermano.save()    
    doc_externo=loader.get_template("plantilla.html")
    documento=doc_externo.render({"Madre_nombre":Madre.nombre,"Madre_edad":Madre.edad,"Madre_documento":Madre.documento,
    "Madre_fecha_nacimiento":Madre.fecha_nacimiento,"Madre_parentezco":Madre.parentezco,"Padre_nombre":Padre.nombre,
    "Padre_edad":Padre.edad,"Padre_documento":Padre.documento,"Padre_fecha_nacimiento":Padre.fecha_nacimiento,"Padre_parentezco":Padre.parentezco,
    "Hermano_nombre":Hermano.nombre,"Hermano_edad":Hermano.edad,"Hermano_documento":Hermano.documento,"Hermano_fecha_nacimiento":Hermano.fecha_nacimiento,"Hermano_parentezco":Hermano.parentezco})
    return HttpResponse(documento)

# Create your views here.
