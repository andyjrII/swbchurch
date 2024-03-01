import django_filters
from .models import Devotional


class DevotionalFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    year = django_filters.NumberFilter(field_name="date__year", lookup_expr="exact")

    class Meta:
        model = Devotional
        fields = ["title", "year"]
