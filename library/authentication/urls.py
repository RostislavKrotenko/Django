from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from author.views import create_author, author_list, delete_author
from order.views import all_orders, my_orders, create_order, close_order
from book.views import all_books, book_detail, filter_books, user_books

urlpatterns = [
    path('register/', views.register, name='register'),
    path('log_in/', views.log_in, name='log_in'),
    path('welcome_user/', TemplateView.as_view(template_name='welcome_user.html'), name='welcome_user'),
    path('welcome_admin/', TemplateView.as_view(template_name='welcome_admin.html'), name='welcome_admin'),
    path('log_out/', views.log_out, name='log_out'),
    path('bye/', TemplateView.as_view(template_name='bye.html'), name='bye'),
    path('success_register/', TemplateView.as_view(template_name='success_register.html'), name='congratulation'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_detail/', views.user_detail, name='user_detail'),
    path('user_manager/', views.return_user_manager, name='user_manager'),
    path('author_manager/', views.return_author_manager, name='author_manager'),
    path('create_author/', create_author, name='create_author'),
    path('author_list/', author_list, name='author_list'),
    path('delete_author', delete_author, name='delete_author'),
    path('all_orders/', all_orders, name='all_orders'),
    path('my_orders/', my_orders, name='my_orders'),
    path('create_order/', create_order, name='create_order'),
    path('close_order/', close_order, name='close_order'),
    path('order_manager/', views.return_order_manager, name='order_manager'),
    path('all_books/', all_books, name='all_books'),
    path('book_detail/', book_detail, name='book_detail'),
    path('filter_books/', filter_books, name='filter_books'),
    path('user_books/', user_books, name='user_books'),
    path('book_manager/', views.return_book_manager, name='book_manager')
]