from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .filters import SermonFilter, NewsEventFilter
from .forms import SearchForm
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
    form = SearchForm(request.GET)
    all_newsevents = NewsEvent.objects.all().order_by("-date_updated")
    news_filter = NewsEventFilter(request.GET, queryset=all_newsevents)
    # pagination
    items_per_page = 12
    paginator = Paginator(news_filter.qs, items_per_page)
    page = request.GET.get("page")
    try:
        paginated_events = paginator.page(page)
    except PageNotAnInteger:
        paginated_events = paginator.page(1)
    except EmptyPage:
        paginated_events = paginator.page(paginator.num_pages)
    context = {
        "form": form,
        "paginated_events": paginated_events,
        "news_filter": news_filter,
    }
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


def sermon_list(request):
    queryset = Sermon.objects.all()
    filter = SermonFilter(request.GET, queryset=queryset)
    return render(request, "sermon_list.html", {"filter": filter})
