from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'publication_year': ['exact', 'gt', 'lt'],
            'author__name': ['exact', 'icontains'],
        }
