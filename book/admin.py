from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'edition', 'country', 'language', 'publisher')
    search_fields = ('title', 'author', 'isbn', 'publisher')
    list_filter = ('publisher', 'author', 'genre', 'country', 'language')
