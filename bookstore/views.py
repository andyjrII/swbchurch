from django.http import HttpResponse
from django.template import loader


def index(request):
    # pylint: disable=no-member
    # latest_newsevents = NewsEvent.objects.order_by("-date_updated")[:3]
    # services = Service.objects.all()
    # context = {"latest_newsevents": latest_newsevents, "services": services}
    template = loader.get_template("bookstore.html")
    return HttpResponse(template.render(request))
