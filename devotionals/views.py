from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import DevotionalFilter
from .forms import SearchForm
from .models import Devotional


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
