from django.http import HttpResponse
from django.template import loader
from .models import NewsEvent


def index(request):
    latest_newsevents = NewsEvent.objects.order_by("-date_updated")[:3]
    context = {"latest_newsevents": latest_newsevents}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))


def newsevents(request):
    all_newsevents = NewsEvent.objects.all().order_by("-date_updated")
    context = {"all_newsevents": all_newsevents}
    template = loader.get_template("newsevents.html")
    return HttpResponse(template.render(context, request))
