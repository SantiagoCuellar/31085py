from re import template
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader


def inicio(request):
    return HttpResponse('Hola soy mi primer vista en django')

def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'Fecha actual: {fecha_actual}')

def saludo(request, nombre):
    return HttpResponse(f'Hola {nombre}!')

# V1

# def mi_template(request):
    
#     archivo = open(r'C:\Users\santi\Desktop\python-31085\DjangoClases\templates\index.html', 'r')

#     template1 = Template(archivo.read())
    
#     contexto1 = Context()
    
#     render1 = template1.render(contexto1)
    
#     return HttpResponse(render1)


# V2

def mi_template(request):
    
    template1 = loader.get_template('index.html')

    render1 = template1.render({})
    
    nombre = "Momia"
    
    return HttpResponse(render1)
    
    
    