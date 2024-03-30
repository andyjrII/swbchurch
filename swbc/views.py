from django.http import HttpResponse
from django.template import loader
from .models import Service
from newsevents.models import NewsEvent


def index(request):
    # pylint: disable=no-member
    latest_newsevents = NewsEvent.objects.order_by("-date_updated")[:3]
    services = Service.objects.all()
    context = {"latest_newsevents": latest_newsevents, "services": services}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))
