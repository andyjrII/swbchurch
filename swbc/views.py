from django.http import HttpResponse
from django.template import loader
from .models import NewsEvent

def testing(request):
    template = loader.get_template('components.html')
    return HttpResponse(template.render())

def index(request):
    latest_newsevents = NewsEvent.objects.order_by('-date_updated')[:3]
    context = {"latest_newsevents": latest_newsevents}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))
