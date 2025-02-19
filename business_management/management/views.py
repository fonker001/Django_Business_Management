from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ClientForm, ProductForm, OrderForm, SignUpForm, TaskForm
from .models import Client, Product, Order, UserProfile, Task  # Add this line to import the models
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib import messages


urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]


@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'management/client_list.html', {'clients': clients})

@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'management/client_detail.html', {'client': client})

@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client created successfully!')
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'management/add_client.html', {'form': form})

@login_required
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client updated successfully!')
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'management/client_form.html', {'form': form})

@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Client deleted successfully!')
        return redirect('client_list')
    return render(request, 'management/client_confirm_delete.html', {'client': client})




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Save additional user information
            UserProfile.objects.create(
                user=user,
                phone_number=form.cleaned_data['phone_number'],
                address=form.cleaned_data['address']
            )
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})




@login_required
def profile(request):
    return render(request, 'management/profile.html')

@login_required
def dashboard(request):
    clients = Client.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()
    tasks = Task.objects.filter(status='pending')  # Fetch pending tasks
    total_revenue = sum(order.total_price for order in orders)

    return render(request, 'management/dashboard.html', {
        'clients': clients,
        'products': products,
        'orders': orders,
        'tasks': tasks,
        'total_revenue': total_revenue,
    })


@login_required
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New order created successfully!')  # Send success notification
            return redirect('dashboard')
    else:
        form = OrderForm()
    return render(request, 'management/add_order.html', {'form': form})

@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'management/order_list.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'management/order_detail.html', {'order': order})

@login_required
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order created successfully!')
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'management/order_form.html', {'form': form})

@login_required
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order updated successfully!')
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'management/order_form.html', {'form': form})

@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Order deleted successfully!')
        return redirect('order_list')
    return render(request, 'management/order_confirm_delete.html', {'order': order})


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'management/product_list.html', {'products': products})

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'management/product_detail.html', {'product': product})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'management/product_form.html', {'form': form})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'management/product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('product_list')
    return render(request, 'management/product_confirm_delete.html', {'product': product})


@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'management/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'management/task_detail.html', {'task': task})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'management/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'management/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')
    return render(request, 'management/task_confirm_delete.html', {'task': task})





