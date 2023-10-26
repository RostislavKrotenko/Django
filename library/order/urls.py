from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_orders, name = 'all_orders'),

    path('create_order/', views.create_order, name='create_order'),
    path('close_order/<int:order_id>/', views.close_order, name='close_order'),


]