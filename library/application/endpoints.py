from rest_framework.generics import \
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book


class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AuthorListCreateAPIView(ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookListCreateAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AuthorRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()




