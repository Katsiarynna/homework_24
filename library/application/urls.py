from django.urls import path
from .endpoints import AuthorListAPIView, BookListAPIView,\
    AuthorListCreateAPIView, BookListCreateAPIView, AuthorRUDAPIView, BookRUDAPIView


urlpatterns = [
    path('author_list/', AuthorListAPIView.as_view(), name="author_list"),
    path('book_list/', BookListAPIView.as_view(), name="book_list"),
    path('author_list_create/', AuthorListCreateAPIView.as_view(), name="author_list_create"),
    path('book_list_create/', BookListCreateAPIView.as_view(), name="book_list_create"),
    path('author_rud/<int:pk>', AuthorRUDAPIView.as_view(), name="author_rud"),
    path('book_rud/<int:pk>', BookRUDAPIView.as_view(), name="book_rud"),
]