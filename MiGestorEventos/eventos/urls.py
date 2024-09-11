"""
URL configuration for MiGestorEventos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import EventoListView, OrganizadorListView, OrganizadorCreateView, EventoCreateView, editar_evento, EventoUpdateView
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('organizadores/', OrganizadorListView.as_view(), name='organizador_list'),
    path('organizadores/nuevo/', OrganizadorCreateView.as_view(), name='organizador_create'),
    path('eventos/', EventoListView.as_view(), name='evento_list'),
    path('eventos/nuevo/', EventoCreateView.as_view(), name='evento_create'),
    path('eventos/editar/<int:evento_id>/', editar_evento, name='editar_evento'),
    path('eventos/actualizar/<int:pk>/', EventoUpdateView.as_view(), name='evento_update'),
]