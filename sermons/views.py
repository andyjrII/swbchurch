from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import SermonFilter
from .forms import SearchForm
from .models import Sermon


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
