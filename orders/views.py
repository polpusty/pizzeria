from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import viewsets

from .forms import NewOrderForm, AddPizzaToOrderForm, StatusPizzaForm
from .models import Pizza, Order, PizzaOrder
from .serializers import PizzaSerializer


def home(request):
    pizzas = Pizza.objects.filter(is_active=True)
    return render(request, 'home.html', {'pizzas': pizzas})


@login_required
def list_orders(request):
    if request.user.is_staff:
        orders = Order.objects.order_by('-date_created')
    else:
        orders = Order.objects.filter(client=request.user).order_by('-date_created')
    return render(request, 'list_orders.html', {'orders': orders})


@login_required
def add_order(request):
    if request.method == 'POST':
        form = NewOrderForm(request.POST)

        if form.is_valid():
            pizza = Pizza.objects.get(pk=form.cleaned_data['pizza'])
            components = pizza.components.all()
            pizza.pk = None
            pizza.is_active = False
            pizza.save()
            pizza.components.add(*components)
            pizza.save()
            order = Order(client=request.user, price=pizza.price)
            order.save()
            order_pizza = PizzaOrder(order=order, pizza=pizza)
            order_pizza.save()
            return redirect('edit_order', order_id=order.id)

    return redirect('home')


@login_required
def details_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'detail_order.html', {'order': order})


@login_required
def editing_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if order.status == 'S' and (request.user.is_staff or order.client == request.user):
        pizzas = Pizza.objects.filter(is_active=True)
        if request.method == 'POST':
            data = request.POST
            for name in data.keys():
                if name != 'csrfmiddlewaretoken':
                    orderpizza = get_object_or_404(PizzaOrder, pk=name)
                    count = int(data[name][0])
                    order.price += (count - orderpizza.count) * orderpizza.pizza.price
                    if count != 0:
                        orderpizza.count = int(data[name][0])
                        orderpizza.save()
                    else:
                        orderpizza.delete()
            order.save()
        return render(request, 'edit_order.html', {'order': order,
                                                   'numbers': range(10),
                                                   'pizzas': pizzas})
    return redirect('details_order', order_id=order.id)


@login_required
def change_status_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = StatusPizzaForm(request.POST)

        if form.is_valid():
            order.status = form.cleaned_data['status']
            order.save()
    return redirect('details_order', order_id=order.id)


@login_required
def add_pizza_to_order(request, order_id):
    if request.method == 'POST':
        form = AddPizzaToOrderForm(request.POST)

        order = get_object_or_404(Order, pk=order_id)

        if order.status != 'S' and (request.user.is_staff or order.client == request.user):
            return redirect('details_order', order_id=order.id)

        if form.is_valid():
            pizza = get_object_or_404(Pizza, pk=form.cleaned_data['pizza'])
            order_pizza = PizzaOrder(order=order, pizza=pizza)
            order.price += pizza.price
            order.save()
            order_pizza.save()
            return redirect('edit_order', order_id=order.id)

    return redirect('home')


class PizzaViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Pizza.objects.filter(is_active=True)
    serializer_class = PizzaSerializer
