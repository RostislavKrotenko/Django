# Create your views here.
import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse

from book.models import Book
from .models import Order
from authentication.models import CustomUser
from .forms import OrderForm


@login_required
@user_passes_test(lambda user: user.is_superuser)
def all_orders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'all_orders.html', context)

@login_required
def my_orders(request):
    user_orders = Order.objects.filter(user=request.user)
    context = {'user_orders': user_orders}
    return render(request, 'my_orders.html', context)

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.data
            plated_end_at = data.get('plated_end_at')
            book = Book.objects.get(pk=data.get('book'))
            Order.create(user=request.user, book=book, plated_end_at=plated_end_at)
            return redirect('my_orders')
    form = OrderForm()
    return render(request, 'create_order.html', {'form': form})

@login_required
@user_passes_test(lambda user: user.is_superuser)
def close_order(request, order_id=None):
    order = Order.get_by_id(order_id)
    if order:
        order.update(end_at=datetime.datetime.now())
        order.delete_by_id(order_id)
        return redirect('all_orders')
    else:
        return render(request, 'all_orders.html', {'error': 'Error closing order.'})