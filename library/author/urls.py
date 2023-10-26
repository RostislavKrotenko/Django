from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'author_urls_app'

urlpatterns = [
    path('new_author/', views.create_author, name='new_author'),
    path('author_list/', views.author_list, name='author_information'),
    path('delete_author/', views.delete_author, name='delete_author')
]