from django.http import HttpResponse
from django.template import loader
from django.core.mail.message import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SearchForm
from .models import Book
from .filters import BookFilter


def bookstore(request):
    # pylint: disable=no-member
    form = SearchForm(request.GET)
    all_books = Book.objects.all().order_by("-date_updated")
    books_filter = BookFilter(request.GET, queryset=all_books)
    # pagination
    items_per_page = 20
    paginator = Paginator(books_filter.qs, items_per_page)
    page = request.GET.get("page")
    try:
        paginated_books = paginator.page(page)
    except PageNotAnInteger:
        paginated_books = paginator.page(1)
    except EmptyPage:
        paginated_books = paginator.page(paginator.num_pages)
    context = {
        "form": form,
        "paginated_books": paginated_books,
        "books_filter": books_filter,
    }
    template = loader.get_template("books.html")
    return HttpResponse(template.render(context, request))


def send_book_via_email(book, user_email):
    subject = f"Your purchased book: {book.title}"
    message = "Thank you for your purchase! Find attached your book file."
    from_email = "ajsly87@gmail.com"  # Replace with your email address

    # Create an EmailMessage instance
    email = EmailMessage(subject, message, from_email, [user_email])

    # Attach the book file to the email
    book_file_path = book.book_file.path
    email.attach_file(
        book_file_path, "application/pdf"
    )  # Adjust the MIME type based on your file type

    # Send the email
    email.send()
