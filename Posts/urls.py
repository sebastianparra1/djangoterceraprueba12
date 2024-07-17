from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<str:pk>/', views.post, name="post"),  # Asegúrate de incluir la barra al final
    path('accounts/', views.login_view, name="sebas"),
    path('tienda/<str:pk>/', views.tienda, name="tienda"),
    path('iniciarsesion/', views.iniciarsesion, name='iniciarsesion'), # este al parecer no sirve
    path('admin/', admin.site.urls),
    path('iniciarsesion/<str:pk>/', views.iniciarsesion, name="iniciarsesion"), # este si sirve, creo...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
