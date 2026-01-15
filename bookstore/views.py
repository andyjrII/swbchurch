from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core.mail.message import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from .forms import SearchForm
from .models import Book
from .filters import BookFilter
from django.views.decorators.csrf import csrf_exempt


def bookstore(request):
    # pylint: disable=no-member
    # Get unique authors from books
    authors = Book.objects.values_list('author', flat=True).distinct().order_by('author')
    
    form = SearchForm(request.GET, authors=authors)
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

@csrf_exempt
def handle_payment_success(request):
    if request.method == 'POST':
        #and request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        # Retrieve data from the AJAX request
        transaction_id = request.POST.get('transaction_id')
        buyer_email = request.POST.get('buyer_email')
        book_id = request.POST.get('book_id')
        
        try:
            # Get the Book object using the book_id
            book = Book.objects.get(pk=book_id)
            
            send_book_via_email(book, buyer_email)
            
            return JsonResponse({'success': True, 'message': 'Book sent successfully'})
        except Book.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Book not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'})


def send_book_via_email(book, buyer_email):
    subject = f"Your purchased book: {book.title}"
    message = "Thank you for your purchase! Find attached your book file."
    from_email = settings.DEFAULT_FROM_EMAIL

    # Create an EmailMessage instance
    email = EmailMessage(subject, message, from_email, [buyer_email])
    
    # Attach the book file to the email
    book_file_path = book.book_file.path
    email.attach_file(
        book_file_path, "application/pdf"
    )  # Adjust the MIME type based on your file type

    # Send the email
    email.send()
