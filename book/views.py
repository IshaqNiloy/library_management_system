from typing import Union, List

from rest_framework.views import APIView

from book.models import Book


class BookView(APIView):
    def __init__(self):
        super().__init__()
        self.model = Book

    def search(self, title: Union[str, None] = None, author: Union[str, None] = None,
               genre: Union[str, None] = None, country: Union[str, None] = None,
               language: Union[str, None] = None, isbn: Union[str, None] = None,
               publisher: Union[str, None] = None) -> List[Book]:
        if title:
            return self.model.objects.search_book()
        if author:
            return self.model.objects.search_book_author()

    def search(self):

    def get(self, request):

