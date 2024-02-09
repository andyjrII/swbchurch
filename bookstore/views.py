from django.http import HttpResponse
from django.template import loader


def bookstore(request):
    # pylint: disable=no-member
    name = {"name": "Andy James", "sex": "Male"}
    context = {"name": name}
    template = loader.get_template("books.html")
    return HttpResponse(template.render(context, request))
