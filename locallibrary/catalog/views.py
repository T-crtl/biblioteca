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

    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    context = {
        'num_books':num_books, 
        'num_instances':num_instances, 
        'num_instances_available':num_instances_available, 
        'num_authors':num_authors, 
        'num_genre':num_genre,
        'num_visits':num_visits,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.all()
    
class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5

    def get_queryset(self):
        return Author.objects.all()
    
class AuthorDetailView(generic.DetailView):
    model = Author