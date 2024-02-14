from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import SermonFilter, NewsEventFilter, DevotionalFilter
from .forms import SearchForm
from .models import NewsEvent, Service, Sermon, Devotional


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
    template = loader.get_template("events.html")
    return HttpResponse(template.render(context, request))


def newsevent_details(request, id):
    # pylint: disable=no-member
    newsevent = NewsEvent.objects.get(id=id)
    latest_newsevents = NewsEvent.objects.order_by("-date_updated")[:4]
    context = {"newsevent": newsevent, "latest_newsevents": latest_newsevents}
    template = loader.get_template("event.html")
    return HttpResponse(template.render(context, request))


def sermons(request):
    # pylint: disable=no-member
    form = SearchForm(request.GET)
    all_sermons = Sermon.objects.all().order_by("-date_preached")
    sermon_filter = SermonFilter(request.GET, queryset=all_sermons)
    # pagination
    items_per_page = 20
    paginator = Paginator(sermon_filter.qs, items_per_page)
    page = request.GET.get("page")
    try:
        paginated_sermons = paginator.page(page)
    except PageNotAnInteger:
        paginated_sermons = paginator.page(1)
    except EmptyPage:
        paginated_sermons = paginator.page(paginator.num_pages)
    context = {
        "form": form,
        "paginated_sermons": paginated_sermons,
        "sermon_filter": sermon_filter,
    }
    template = loader.get_template("sermons.html")
    return HttpResponse(template.render(context, request))


def devotionals(request):
    # pylint: disable=no-member
    form = SearchForm(request.GET)
    all_devotionals = Devotional.objects.all().order_by("-date")
    devotional_filter = DevotionalFilter(request.GET, queryset=all_devotionals)
    # pagination
    items_per_page = 10
    paginator = Paginator(devotional_filter.qs, items_per_page)
    page = request.GET.get("page")
    try:
        paginated_devotionals = paginator.page(page)
    except PageNotAnInteger:
        paginated_devotionals = paginator.page(1)
    except EmptyPage:
        paginated_devotionals = paginator.page(paginator.num_pages)
    context = {
        "form": form,
        "paginated_devotionals": paginated_devotionals,
        "devotional_filter": devotional_filter,
    }
    template = loader.get_template("devotionals.html")
    return HttpResponse(template.render(context, request))


def devotional_details(request, id):
    # pylint: disable=no-member
    devotional = Devotional.objects.get(id=id)
    latest_devotionals = Devotional.objects.order_by("-date")[:4]
    context = {"devotional": devotional, "latest_devotionals": latest_devotionals}
    template = loader.get_template("devotional.html")
    return HttpResponse(template.render(context, request))
