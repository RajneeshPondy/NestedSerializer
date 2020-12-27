from django.urls import path
from .views import (
    AuthorListAPIView,
    AuthorDetailAPIView,
    BookListAPIView,
    BookDetailAPIView,
)

urlpatterns = [
    path("author", AuthorListAPIView.as_view()),
    path("author/<int:pk>", AuthorDetailAPIView.as_view()),
    path("book", BookListAPIView.as_view()),
    path("book/<int:pk>", BookDetailAPIView.as_view()),
]
