from django.http import HttpResponse
from django.template import loader
from .models import Service
from newsevents.models import NewsEvent


def index(request):
    # pylint: disable=no-member
    latest_newsevents = NewsEvent.objects.order_by("-date_updated")[:3]
    
    # Get weekly and special services from database
    weekly_services = Service.objects.filter(service_type='weekly')
    special_services = Service.objects.filter(service_type='special')
    
    # Fallback data for weekly services if none exist
    # Store relative path - template will use {% static %} tag
    default_weekly_services = [
        {
            'title': 'Sunday Service',
            'day': 'Sundays',
            'time': '8:00AM',
            'feature_pic_path': 'assets/imgs/services-1.jpg',
            'is_default': True,
        },
        {
            'title': 'Prayer Meeting',
            'day': 'Wednesdays',
            'time': '5:30PM',
            'feature_pic_path': 'assets/imgs/services-2.jpg',
            'is_default': True,
        },
        {
            'title': 'Mission is Possible',
            'day': 'Saturdays',
            'time': '10:00AM',
            'feature_pic_path': 'assets/imgs/services-3.jpg',
            'is_default': True,
        },
        {
            'title': 'Word Drill',
            'day': 'Last Saturdays',
            'time': '7:00AM',
            'feature_pic_path': 'assets/imgs/services-4.jpg',
            'is_default': True,
        },
    ]
    
    # Use database services if available, otherwise use fallback
    if weekly_services.exists():
        weekly_services_list = weekly_services
        use_default_weekly = False
    else:
        weekly_services_list = default_weekly_services
        use_default_weekly = True
    
    context = {
        "latest_newsevents": latest_newsevents,
        "weekly_services": weekly_services_list,
        "use_default_weekly": use_default_weekly,
        "special_services": special_services,
    }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))
