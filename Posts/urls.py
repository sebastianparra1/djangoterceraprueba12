from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/',views.login_view, name="sebas") ,
    path('iniciarsesion/', views.iniciarsesion, name='iniciarsesion'),
    path('admin/', admin.site.urls),
]