import json
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .models import Product
from .models import Contact
from .models import Cart, CartItem
# from .models import Hoodie
# from .models import Cargo
# from .models import Jean
# from .models import Oversize
# from .models import Jacket
# from .models import RegUser


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        myuser = User.objects.create_user(username, firstname, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()

        messages.success(request, "your account has been successfully created")
        return redirect('signin')

    return render(request, 'products/signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            return redirect('products')
        else:
            messages.error(
                request, "Wrong Email or Password, Please try again!")
            return redirect('signin')
    return render(request, 'products/signin.html')


def signout(request):
    logout(request)
    # messages.success(request, "Signed out successfully!")
    return render(request, 'products/products.html')


def cart(request):
    context = {}
    return render(request, 'products/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'products/checkout.html', context)


def typage(request):
    context = {}
    return render(request, 'products/typage.html', context)


def typage2(request):
    context = {}
    return render(request, 'products/typage2.html', context)


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
        return render(request, 'products/typage2.html')

    return render(request, 'products/contactus.html', {})


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


def products(request):
    prod = Product.objects.all()
    prohood = prod.filter(category='Hoodie')
    procarg = prod.filter(category='Cargo')
    projean = prod.filter(category='Jeans')
    proover = prod.filter(category='Oversize')
    projack = prod.filter(category='Jacket')

    # hood = Hoodie.objects.all()
    # x = {'hoodie': hood.filter()}
    # carg = Cargo.objects.all()
    # z = {'cargo': carg.filter()}
    # jean = Jean.objects.all()
    # oversize = Oversize.objects.all()
    # jacket = Jacket.objects.all()
    # all = {'hoodie': hood, 'cargo': carg, 'jeans': jean,
    #        'oversize': oversize, 'jacket': jacket}
    return render(request, 'products/products.html', {'hoodie': prohood, 'cargo': procarg, 'jeans': projean,
                                                      'oversize': proover, 'jacket': projack})
