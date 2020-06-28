from django.urls import path, re_path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$',
            views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$',
            views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.AllBorrowedBooksListView.as_view(), name='all-borrowed'),

    path('book/<uuid:pk>/renew/', views.renew_book_librarian,
         name='renew-book-librarian'),

    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<uuid:pk>/update', views.BookUpdate.as_view(), name='book_update'),
    path('book/<uuid:pk>/delete', views.BookUpdate.as_view(), name='book_delete'),
    
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete', views.AuthorDelete.as_view(), name='author_delete'),
]
