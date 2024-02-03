- Page for downloading reports formats
- Date and text search filter for events & sermons
- work on error page
- Payment Gateway
- Add modal/popup to each image in the gallery to make then bigger
- Find a way to put <pre> element for content details from DB
- E-Book sales Section
- Daily Devotional Section

###########################
Admin login
###########################

username: andyjames
email: ajsly87@gmail.com
password: SlyF0x@87

###########################
Search Filter
###########################

To implement search filters for the `Sermon` and `NewsEvent` classes in Django, you can use the `django-filter` library. This library allows you to easily create filters for your models.

First, you need to install the `django-filter` library:

```bash
pip install django-filter
```

Next, you can create a `filters.py` file in your app directory and define the filters for each model:

```python
# filters.py
import django_filters
from .models import Sermon, NewsEvent

class SermonFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    date_preached = django_filters.DateFilter()

    class Meta:
        model = Sermon
        fields = ['title', 'date_preached']

class NewsEventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    date_published = django_filters.DateFilter()

    class Meta:
        model = NewsEvent
        fields = ['title', 'date_published']
```

Then, in your views where you want to use these filters, you can apply them like this:

```python
# views.py
from django.shortcuts import render
from django_filters.views import FilterView
from .models import Sermon, NewsEvent
from .filters import SermonFilter, NewsEventFilter

def sermon_list(request):
    queryset = Sermon.objects.all()
    filter = SermonFilter(request.GET, queryset=queryset)
    return render(request, 'sermon_list.html', {'filter': filter})

def news_event_list(request):
    queryset = NewsEvent.objects.all()
    filter = NewsEventFilter(request.GET, queryset=queryset)
    return render(request, 'news_event_list.html', {'filter': filter})
```

Finally, in your respective HTML templates (`sermon_list.html` and `news_event_list.html`), you can render the filters and display the filtered results.

Here's an example snippet for `sermon_list.html`:

```html
{% block content %}
<h1>Sermons</h1>
<form method="get">
  {{ filter.form.as_p }}
  <button type="submit">Filter</button>
</form>
<ul>
  {% for sermon in filter.qs %}
  <li>{{ sermon.title }} - {{ sermon.date_preached }}</li>
  {% endfor %}
</ul>
{% endblock %}
```

And a similar one for `news_event_list.html`:

```html
{% block content %}
<h1>News Events</h1>
<form method="get">
  {{ filter.form.as_p }}
  <button type="submit">Filter</button>
</form>
<ul>
  {% for news_event in filter.qs %}
  <li>{{ news_event.title }} - {{ news_event.date_published }}</li>
  {% endfor %}
</ul>
{% endblock %}
```

This way, users can search for sermons or news events based on the specified fields. Adjust the templates and styling as needed for your project.
