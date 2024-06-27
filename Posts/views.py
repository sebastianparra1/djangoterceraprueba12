# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Cart, Productosssss

@login_required
def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'Posts/posts_page.html', context)

@login_required
def post(request, pk):
    post = get_object_or_404(Post, id=pk)
    context = {'post': post}
    return render(request, 'Posts/post.html', context)

@login_required
def cart(request):
    cart_obj, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart_obj.items.all()
    context = {'cart_items': cart_items}
    return render(request, 'cart.html', context)

@login_required
def add_to_cart(request, pk):
    post = get_object_or_404(Post, id=pk)
    cart_obj, _ = Cart.objects.get_or_create(user=request.user)
    cart_obj.items.add(post)
    return redirect('cart')

@login_required
def remove_from_cart(request, pk):
    post = get_object_or_404(Post, id=pk)
    cart_obj, _ = Cart.objects.get_or_create(user=request.user)
    cart_obj.items.remove(post)
    return redirect('cart')

def cart_view(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    context = {'cart': cart}
    return render(request, 'cart.html', context)

def login_view(request):
    return render(request, 'registration/login.html')

def tienda(request, pk):
    tienda = Post.objects.get(id=pk)
    context ={'tienda': tienda }
    return render(request, 'Posts/tienda.html')

def tienda_view(request):
    productos =  Productosssss.objects.all()
    print(productos) #borra si no sirve
    return render(request, 'tienda.html', {'productos': productos})







