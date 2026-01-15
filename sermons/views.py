from django.http import HttpResponse, Http404, FileResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from .filters import SermonFilter
from .forms import SearchForm
from .models import Sermon


def sermons(request):
    # pylint: disable=no-member
    # Get unique authors from sermons
    authors = Sermon.objects.values_list('author', flat=True).distinct().order_by('author')
    
    form = SearchForm(request.GET, authors=authors)
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
    
    # Get weekly top sermons (most recent 6 with audio)
    top_sermons = Sermon.objects.filter(
        audio_file__isnull=False
    ).order_by("-date_preached")[:6]
    
    context = {
        "form": form,
        "paginated_sermons": paginated_sermons,
        "sermon_filter": sermon_filter,
        "top_sermons": top_sermons,
    }
    template = loader.get_template("sermons.html")
    return HttpResponse(template.render(context, request))


def download_sermon(request, sermon_id):
    """Download sermon audio file from Cloudinary"""
    sermon = get_object_or_404(Sermon, pk=sermon_id)
    
    if not sermon.audio_file:
        raise Http404("Audio file not available for this sermon")
    
    # For Cloudinary files, we redirect to the Cloudinary URL
    # The file will be served directly from Cloudinary
    audio_url = sermon.audio_file.url
    
    # Return a redirect response to the Cloudinary URL
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect(audio_url)
