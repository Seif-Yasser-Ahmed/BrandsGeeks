from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import datetime
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Signupp(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    prohood = products.filter(category='Hoodie')
    procarg = products.filter(category='Cargo')
    projean = products.filter(category='Jeans')
    proover = products.filter(category='Oversize')
    projack = products.filter(category='Jacket')
    context = {'products': products, 'hoodie': prohood, 'cargo': procarg, 'jeans': projean,
               'oversize': proover, 'jacket': projack, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        print('cart: ', cart)
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

        for i in cart:
            cartItems += cart[i]['quantity']
            product = Product.objects.get(id=1)
            total = (product.price*cart[i]["quantity"])
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]
            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL
                },
                'quantity': cart[i]['quantity'],
                'get_total': total,
            }
            items.append(item)

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action: ', action)
    print('productId: ', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity-1)
    elif action == 'remove-all':
        orderItem.quantity = 0

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                country=data['shipping']['country'],
                zipcode=data['shipping']['zipcode'],
            )
    else:
        print('user is not logged in')
    return JsonResponse('Payment complete', safe=False)


def signup(request):
    form = Signupp()

    if request.method == "POST":
        form = Signupp(request.POST)
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            messages.success(request, 'Account was created for: '+name)
            Customer.objects.create(user=user,
                                    name=name, email=email)
            return redirect('signin')
    context = {'form': form}
    return render(request, 'store/signup.html', context)


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            return redirect('store')
        else:
            messages.error(
                request, "Wrong Email or Password, Please try again!")
            return redirect('signin')
    return render(request, 'store/signin.html')


def logoutUser(request):
    logout(request)
    return redirect('signin')


def typage(request):
    context = {}
    return render(request, 'store/typage.html', context)


def typage2(request):
    context = {}
    return render(request, 'store/typage2.html', context)


def contactus(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return render(request, 'store/typage2.html')

    return render(request, 'store/contactus.html', {})


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get_or_create(user=request.user, completed=False)
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(
            user=request.user, completed=False)
        print(cart)
        # CartItem.quantity = CartItem.quantity + 1
        # CartItem.save()
        # cartitem, created = CartItem.objects.get_or_create(
        #     cart=cart, hoodie=hoodie)
        # print(cartitem)
    return JsonResponse("it's working", safe=False)
