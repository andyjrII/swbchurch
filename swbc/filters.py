import django_filters
from .models import Sermon, NewsEvent, Devotional


class SermonFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    year_preached = django_filters.NumberFilter(
        field_name="date_preached__year", lookup_expr="exact"
    )

    class Meta:
        model = Sermon
        fields = ["title", "year_preached"]


class NewsEventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    year_published = django_filters.NumberFilter(
        field_name="date_published__year", lookup_expr="exact"
    )

    class Meta:
        model = NewsEvent
        fields = ["title", "year_published"]


class DevotionalFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    year = django_filters.NumberFilter(field_name="date__year", lookup_expr="exact")

    class Meta:
        model = Devotional
        fields = ["title", "year"]
