from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'language', 'display_genre')
    inlines = [BookInstanceInline]

class BookInstanceAuthorInline(admin.TabularInline):
    model = Book

#admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInstanceAuthorInline]

admin.site.register(Genre)

#admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )

admin.site.register(Language)