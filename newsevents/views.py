from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import NewsEventFilter
from .forms import SearchForm
from .models import NewsEvent


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
