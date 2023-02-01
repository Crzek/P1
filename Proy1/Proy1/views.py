from django.http import HttpResponse

import datetime


def toh1(request, tag="h1"):
  doc = f"""
  <html>
  <body>
  <{tag}>
  {request}
  </{tag}>
  </body>
  </html>
  """
  return doc

def saludo(request):      #1r view
  doc = """
  <html>
  <body>
  <h1>
  Primera paguina con Django
  </h1>
  </body>
  </html>
  """
  return HttpResponse(doc)

def despedida(request):
  return HttpResponse("Nos vemos, Adios")

def date(request):
  return datetime.datetime.now()

