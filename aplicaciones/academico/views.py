#from django.http import HttpResponse
from .models import carrera, curso
from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib import messages

def home(request):
  #  return HttpResponse("<h1>hola mundo</h1>")
  cursos=curso.objects.all()
  messages.success(request,"!cursos listados")
  #cursos=curso.objects.filter(nombre='ingles')
  #cursos=curso.objects.filter(creditos__lte=5)
  #cursos=curso.objects.filter(nombre__startswith='i')
  #cursos=curso.objects.filter(nombre__contains='g')
  dato = {
    'titulo':'gestion de cursos',
    'cursos':cursos
  }
  #return render(request,"gestion.html",{"cursos":cursos})
  return render(request,"gestion.html",dato)

class cursolistview(ListView):
  model= curso
  template_name= 'gestion.html'

  def get_context_data(self, **kwargs):
      context= super().get_context_data(**kwargs)
      context['titulo']='gestion de cursos'
      #print(context)
      return context


def eliminar_curso(request,id):
  cursos=curso.objects.get(id=id)
  cursos.delete()

  messages.success(request,"curso eliminado")
  return redirect('/')

def registrar_curso(request):
  nombre=request.POST['txtname']
  creditos=request.POST['numcreditos']

  cursos=curso.objects.create(nombre=nombre,creditos=creditos)
  messages.success(request,"registro exitoso")
  return redirect('/')

def edicion_curso(request,id): #esto funciona para leer un curso y redirigirte a otra pagina para hacer la edicion
  cursos=curso.objects.get(id=id)
  dato = {
    'titulo':'editar curso',
    'cursos':cursos
  }
  return render(request,"edicioncurso.html",dato)

def editar_curso(request):
  id=int(request.POST['id'])
  nombre=request.POST['txtname']
  creditos=request.POST['numcreditos']

  cursos=curso.objects.get(id=id)
  cursos.nombre=nombre
  cursos.creditos=creditos
  cursos.save()

  messages.success(request,"edicion exitoso")
  return redirect('/')

def contacto(request):
  
  return render(request,"contacto.html")

class carreralistview(ListView):
  model= carrera
  template_name= 'carreras.html'

  def get_context_data(self, **kwargs):
      context= super().get_context_data(**kwargs)
      context['titulo']='carreras'
      #print(context)
      return context