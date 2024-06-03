from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publisher')
    search_fields = ('title', 'author', 'publisher')
    list_filter = ('publisher', 'author')
