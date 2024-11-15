from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()
    num_authors = Author.objects.count()
    num_genre = Genre.objects.count()

    return render(request, 'index.html', 
                  context={'num_books':num_books, 'num_instances':num_instances, 
                           'num_instances_available':num_instances_available, 
                           'num_authors':num_authors, 'num_genre':num_genre})

class BookListView(generic.ListView):
    model = Book
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.all()
    
class BookDetailView(generic.DetailView):
    model = Book