import django_filters
from .models import Sermon


class SermonFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    author = django_filters.CharFilter(lookup_expr="icontains")
    year_preached = django_filters.NumberFilter(
        field_name="date_preached__year", lookup_expr="exact"
    )

    class Meta:
        model = Sermon
        fields = ["title", "author", "year_preached"]
