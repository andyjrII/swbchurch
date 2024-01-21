from django.http import HttpResponse
from django.template import loader

def testing(request):
    template = loader.get_template('components.html')
    return HttpResponse(template.render())

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())