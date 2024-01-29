from django.http import HttpResponse
from django.template import loader
from .models import NewsEvent
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    latest_newsevents = NewsEvent.objects.order_by("-date_updated")[:3]
    context = {"latest_newsevents": latest_newsevents}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))


def newsevents(request):
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
    newsevent = NewsEvent.objects.get(id=id)
    latest_newsevents = NewsEvent.objects.order_by("-date_updated")[:4]
    context = {"newsevent": newsevent, "latest_newsevents": latest_newsevents}
    template = loader.get_template("news_post.html")
    return HttpResponse(template.render(context, request))
