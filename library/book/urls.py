from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.all_books),
    path('<int:book_id>', views.book_detail, name='one_book'),
    path('filter/', views.filter_books, name='filter_books'),
    path('user_books/<int:user_id>/', views.user_books, name='user_books'),
    path('add/', views.add_book, name='add'),
    path('edit/<int:book_id>/', views.edit_book, name='edit'),
    path('delete/<int:book_id>/', views.delete_book, name='delete'),
]