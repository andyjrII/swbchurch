import django_filters
from .models import NewsEvent


class NewsEventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    year_published = django_filters.NumberFilter(
        field_name="date_published__year", lookup_expr="exact"
    )

    class Meta:
        model = NewsEvent
        fields = ["title", "year_published"]
