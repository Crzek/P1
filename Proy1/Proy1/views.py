from django.http import HttpResponse
from django.template import Template, Context #caragr de forma manual 
from django.template import loader    #cargador

import datetime


class Person:

  def __init__(self, name, last_name) -> None:
    self.name = name
    self.l_name = last_name

def calculaedad(request, age, year):
  #age = 26
  pediod = year - 2023
  futuryear = age + pediod
  doc = f"En el año {year} tendras {futuryear}","h2"
  return HttpResponse(doc)

def saludo(request):      #1r view


  #nombre = "Erick"
  persona = Person("Javier", "Cruz")

  fecha = datetime.datetime.now()
  #apellido = "Cruz"

  #Cargamos template de forma Manual
  '''
  doc_externo = open("C:/Users/ERICK/Documents/Desarrollo/python/Django/P1/Proy1/Proy1/plantillas/mitemplate.html")
  plt = Template(doc_externo.read())   #creaomos platilla y que la lea
  doc_externo.close()   #cerramos
  '''

  #Cargamos Template con cargador
  plt = loader.get_template("mitemplate.html")

  #creamos contexto si lo cargamos de forma Manual
  '''
  ctx = Context(
    {
    "nombre_persona":persona.name,
    "apellido_persona":"Cruz",
    "momento_ahora":fecha,
    "Temas":[
      "Plantillas",
      "Modelos",
      "Formularios",
      "Vistas",
      "Despliegue"
      ]
  })       
  '''

  #renderizamos el contexto de forma manual
  #doc = plt.render(ctx)  

  # Renderizamos Contexto Con Loader, se ha de pasar directament el diccionario
  doc = plt.render(
    {
    "nombre_persona":persona.name,
    "apellido_persona":"Cruz",
    "momento_ahora":fecha,
    "Temas":[
      "Plantillas",
      "Modelos",
      "Formularios",
      "Vistas",
      "Despliegue"
      ]
    }
  )


  return HttpResponse(doc)

def despedida(request):     #2n VIEW
  return HttpResponse("Nos vemos, Adios")

def date(request):          #3r VIEW
  return HttpResponse(datetime.datetime.now())

