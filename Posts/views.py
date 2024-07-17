# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Cart, Productosssss 
import requests
from datetime import datetime
 

def home(request):
    print("Entrando a mi_vista", request)
    posts = Post.objects.all()
    print(posts)
    fecha_hora = obtener_fecha_hora()
    context = {'posts': posts, "fecha_hora": fecha_hora }
    print(context)
    return render(request, 'posts_page.html', context)


def post(request, pk):
    post = get_object_or_404(Post, id=pk)
    fecha_hora = obtener_fecha_hora()
    context ={'post': post, "fecha_hora": fecha_hora }
    return render(request, 'Posts/post.html', context)


def cart(request):
    cart_obj, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart_obj.items.all()
    context = {'cart_items': cart_items}
    return render(request, 'cart.html', context)


def add_to_cart(request, pk):
    post = get_object_or_404(Post, id=pk)
    cart_obj, _ = Cart.objects.get_or_create(user=request.user)
    cart_obj.items.add(post)
    return redirect('cart')


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
    return render(request, 'Posts/templates/iniciarsesion.html')

def tienda(request, pk):
    post = Post.objects.get(id=pk)
    fecha_hora = obtener_fecha_hora()
    context ={'post': post, "fecha_hora": fecha_hora }
    return render(request, 'Posts/tienda.html', context)

def iniciarsesion(request, pk):
    iniciarsesion = get_object_or_404(Post, id=pk)  
    context = {'iniciarsesion': iniciarsesion}  
    return render(request, 'Posts/iniciarsesion.html', context)  

def obtener_fecha_hora():
    url = "http://worldtimeapi.org/api/timezone/America/Santiago"
    response = requests.get(url)
    data = response.json()
    
    datetime_format_iso = datetime.fromisoformat(data['datetime'])
    
    return datetime_format_iso.strftime('%d-%m-%Y %H:%M:%S')


