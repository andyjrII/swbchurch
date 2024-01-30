from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import NewsEvent, Service, Sermon


def index(request):
    # pylint: disable=no-member
    latest_newsevents = NewsEvent.objects.order_by("-date_updated")[:3]
    services = Service.objects.all()
    context = {"latest_newsevents": latest_newsevents, "services": services}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))


def newsevents(request):
    # pylint: disable=no-member
    all_newsevents = NewsEvent.objects.all().order_by("-date_updated")
    items_per_page = 12
    paginator = Paginator(all_newsevents, items_per_page)
    page = request.GET.get("page")
    try:
        paginated_events = paginator.page(page)
    except PageNotAnInteger:
        paginated_events = paginator.page(1)
    except EmptyPage:
        paginated_events = paginator.page(paginator.num_pages)
    context = {"paginated_events": paginated_events}
    template = loader.get_template("all_events.html")
    return HttpResponse(template.render(context, request))


def details(request, id):
    # pylint: disable=no-member
    newsevent = NewsEvent.objects.get(id=id)
    latest_newsevents = NewsEvent.objects.order_by("-date_updated")[:4]
    context = {"newsevent": newsevent, "latest_newsevents": latest_newsevents}
    template = loader.get_template("event_details.html")
    return HttpResponse(template.render(context, request))


def sermons(request):
    # pylint: disable=no-member
    all_sermons = Sermon.objects.all().order_by("-date_preached")
    items_per_page = 20
    paginator = Paginator(all_sermons, items_per_page)
    page = request.GET.get("page")
    try:
        paginated_sermons = paginator.page(page)
    except PageNotAnInteger:
        paginated_sermons = paginator.page(1)
    except EmptyPage:
        paginated_sermons = paginator.page(paginator.num_pages)
    context = {"paginated_sermons": paginated_sermons}
    template = loader.get_template("sermons.html")
    return HttpResponse(template.render(context, request))
