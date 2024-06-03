from django.utils import timezone

from django.db import models
from django_countries.fields import CountryField
from .choices import ORDINAL_CHOICES, GENRE_CHOICES, LANGUAGES


class Book(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    author = models.CharField(max_length=250, null=False, blank=False)
    genre = models.CharField(choices=GENRE_CHOICES, null=False, blank=False)
    edition = models.CharField(choices=ORDINAL_CHOICES, null=False, blank=False)
    pages = models.IntegerField(null=False, blank=False)
    country = CountryField(null=False, blank=False)
    language = models.CharField(choices=LANGUAGES, null=False, blank=False)
    isbn = models.CharField(max_length=20, null=False, blank=False)
    publisher = models.CharField(max_length=250, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['title', 'author']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        db_table = 'book'

    def __str__(self):
        return f'{self.title} by {self.author}'























